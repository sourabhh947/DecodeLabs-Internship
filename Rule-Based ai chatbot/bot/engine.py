from config import (
    RESPONSES, EXIT_KEYWORDS, FALLBACK,
    BOT_NAME, BOT_VERSION, BOT_ORG, BOT_BATCH,
)
from utils import sanitize, is_empty


def show_banner():
    print("\n" + "=" * 54)
    print(f"   🤖  {BOT_NAME} — {BOT_ORG} AI Chatbot  v{BOT_VERSION}")
    print(f"   📦  Project 1 | Rule-Based Intelligence")
    print(f"   🎓  Batch {BOT_BATCH} | Industrial Training")
    print(f"   💡  Type 'help' to see what I can do")
    print(f"   🚪  Type 'exit' or 'quit' to stop")
    print("=" * 54 + "\n")


def show_farewell():
    print("\n" + "=" * 54)
    print(f"   👋  Session ended. Thanks for using {BOT_NAME}!")
    print(f"   🚀  Built by a {BOT_ORG} AI Intern | Batch {BOT_BATCH}")
    print("=" * 54 + "\n")


def show_response(reply):
    print(f"{BOT_NAME}: {reply}\n")


import datetime

def get_response(clean_input):

    # DATE keywords
    if clean_input in ("date", "what is date", "what is today", "today", "today's date", "what is the date"):
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Today is {today}."

    # TIME keywords
    if clean_input in ("time", "what is time", "what time is it", "current time", "what is the time"):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"Current time is {now}."

    # DAY keyword
    if clean_input in ("day", "what day is it", "which day"):
        day = datetime.datetime.now().strftime("%A")
        return f"Today is {day}."

    # Default dictionary lookup
    return RESPONSES.get(clean_input, FALLBACK)


def is_exit_command(clean_input):
    return clean_input in EXIT_KEYWORDS


def process(raw_input):
    clean = sanitize(raw_input)

    if is_empty(clean):
        show_response("Please type something! (Type 'help' for options)")
        return True

    if is_exit_command(clean):
        show_farewell()
        return False

    reply = get_response(clean)
    show_response(reply)
    return True