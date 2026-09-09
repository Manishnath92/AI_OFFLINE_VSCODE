from llama_cpp import Llama
from datetime import datetime
import json
import os
import re
import asyncio
from queue import Queue
from threading import Thread

# -------- AI MODEL LOAD --------
CPU_THREADS = max(1, (os.cpu_count() or 2) - 1)
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi-2.Q4_K_M.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=1024,
    n_batch=512,
    n_ubatch=512,
    n_threads=CPU_THREADS,
    n_threads_batch=CPU_THREADS,
    use_mmap=True,
    offload_kqv=True,
    flash_attn=True,
    verbose=False
)

# -------- MEMORY SETUP --------
MEMORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory", "memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(mem):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=2, ensure_ascii=False)

def add_memory(text):
    mem = load_memory()
    mem.append({
        "text": text,
        "time": datetime.now().isoformat()
    })
    save_memory(mem)

# -------- MEMORY FILTER (IMPORTANT) --------
def get_clean_memory(limit=5):
    mem = load_memory()
    clean = []
    for m in mem:
        t = m["text"].lower()
        if any(bad in t for bad in ["example:", "question:", "reply to this"]):
            continue
        clean.append(m["text"])
    return clean[-limit:]

# -------- MEMORY RULES --------
def should_remember(text):
    keywords = [
        "i want to learn",
        "i want to become",
        "my goal",
        "my plan",
        "my dream"
    ]
    text = text.lower()
    return any(k in text for k in keywords)

# -------- NAME DETECT --------
def detect_name(text):
    match = re.match(r"(?:my name is|i am)\s+([\w'-]+)\s*[.!?]*$", text.strip(), re.IGNORECASE)
    if match:
        return match.group(1).capitalize()
    return None

# -------- NAME RECALL --------
def get_saved_name():
    for m in reversed(load_memory()):
        text = m.get("text", "")
        match = re.fullmatch(r"user name is\s+(.+?)\s*[.!?]*", text, re.IGNORECASE)
        if match:
            return match.group(1).strip().capitalize()
    return None

async def stream_response(prompt):
    """Generate in a worker thread while the asyncio loop remains responsive."""
    chunks = Queue()

    def generate():
        try:
            for output in llm(
                prompt,
                max_tokens=96,
                temperature=0.6,
                top_p=0.9,
                stop=["User:", "You:"],
                stream=True
            ):
                chunks.put(output["choices"][0]["text"])
        except Exception as error:
            chunks.put(error)
        finally:
            chunks.put(None)

    Thread(target=generate, daemon=True).start()
    reply_parts = []
    while True:
        chunk = await asyncio.to_thread(chunks.get)
        if chunk is None:
            break
        if isinstance(chunk, Exception):
            raise chunk
        print(chunk, end="", flush=True)
        reply_parts.append(chunk)
    print()
    return "".join(reply_parts).strip()


async def chat_loop():
    print("🤖 SHADOW AI READY (OFFLINE + MEMORY)")
    print("Type 'bye' to quit\n")

    while True:
        user = (await asyncio.to_thread(input, "You: ")).strip()

        if not user:
            continue

        if user.lower() == "bye":
            print("AI: Bye! Jo bola hai wo yaad rahega 😏")
            break

        if user.lower() in ["hi", "hello", "hey"]:
            print("AI: Hi 👋 bolo, kya help chahiye?")
            continue

        name = detect_name(user)
        if name:
            add_memory(f"User name is {name}")
            print(f"AI: Nice to meet you, {name} 😊")
            continue

        if re.fullmatch(r"(?:what is|tell me) my name\??", user.strip(), re.IGNORECASE):
            saved_name = get_saved_name()
            if saved_name:
                print(f"AI: Tumhara naam {saved_name} hai 🙂")
            else:
                print("AI: Tumne abhi tak apna naam nahi bataya 😅")
            continue

        if user.lower() in ["what", "what is i learn", "what is i make"]:
            print("AI: Thoda clearly pucho 😅 example: 'what should I learn?'")
            continue

        if should_remember(user):
            add_memory(user)

        memory_context = "\n".join(f"- {m}" for m in get_clean_memory())
        prompt = f"""Background info about the user:
{memory_context}

Answer simply and correctly.

User: {user}
AI:"""

        print("AI: ", end="", flush=True)
        reply = await stream_response(prompt)
        if not reply:
            print("Isko thoda detail me pucho 🙂")


if __name__ == "__main__":
    asyncio.run(chat_loop())
