from llama_cpp import Llama
from datetime import datetime
import json
import os
import re

# -------- AI MODEL LOAD --------
llm = Llama(
    model_path="phi-2.Q4_K_M.gguf",
    n_ctx=2048,
    verbose=False
)

# -------- MEMORY SETUP --------
MEMORY_FILE = "memory/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(mem):
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
    match = re.match(r"my name is (\w+)", text.lower())
    if match:
        return match.group(1).capitalize()
    return None

# -------- NAME RECALL --------
def get_saved_name():
    for m in reversed(load_memory()):
        if m["text"].lower().startswith("user name is"):
            return m["text"].split("is")[-1].strip().capitalize()
    return None

print("🤖 SHADOW AI READY (OFFLINE + MEMORY)")
print("Type 'bye' to quit\n")

# -------- CHAT LOOP --------
while True:
    user = input("You: ").strip()

    if not user:
        continue

    if user.lower() == "bye":
        print("AI: Bye! Jo bola hai wo yaad rahega 😏")
        break

    # -------- GREETING --------
    if user.lower() in ["hi", "hello", "hey"]:
        print("AI: Hi 👋 bolo, kya help chahiye?")
        continue

    # -------- NAME SAVE --------
    name = detect_name(user)
    if name:
        add_memory(f"User name is {name}")
        print(f"AI: Nice to meet you, {name} 😊")
        continue

    # -------- NAME QUESTION --------
    if user.lower() in ["what is my name", "tell me my name"]:
        saved_name = get_saved_name()
        if saved_name:
            print(f"AI: Tumhara naam {saved_name} hai 🙂")
        else:
            print("AI: Tumne abhi tak apna naam nahi bataya 😅")
        continue

    # -------- BROKEN QUESTIONS --------
    if user.lower() in ["what", "what is i learn", "what is i make"]:
        print("AI: Thoda clearly pucho 😅 example: 'what should I learn?'")
        continue

    # -------- SAVE MEMORY --------
    if should_remember(user):
        add_memory(user)

    # -------- LOAD CLEAN MEMORY --------
    memory_context = "\n".join(f"- {m}" for m in get_clean_memory())

    # -------- PROMPT --------
    prompt = f"""Background info about the user:
{memory_context}

Answer simply and correctly.

User: {user}
AI:"""

    output = llm(
        prompt,
        max_tokens=180,   # balanced, not too high
        temperature=0.6,
        stop=["User:", "You:"]
    )

    reply = output["choices"][0]["text"].strip()
    if not reply:
        reply = "Isko thoda detail me pucho 🙂"

    print("AI:", reply)
