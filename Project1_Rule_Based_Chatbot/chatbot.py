# ==========================================
# Project 1: Rule-Based AI Chatbot
# Author: Poonam Nana Patil
# ==========================================

import datetime

# Knowledge Base (Dictionary)
responses = {
    "hello": "Hello! Nice to meet you.",
    "hi": "Hi there! 👋",
    "hey": "Hey! Welcome.",
    "good morning": "Good Morning! Have a wonderful day.",
    "good afternoon": "Good Afternoon!",
    "good evening": "Good Evening!",
    "how are you": "I'm doing great. Thanks for asking!",
    "your name": "I am RuleBot, a Rule-Based AI Chatbot.",
    "ai": "Artificial Intelligence enables machines to learn and solve problems.",
    "python": "Python is a powerful programming language used in AI, Data Science, and Web Development.",
    "internship": "DecodeLabs internship helps you build practical AI projects.",
    "thank you": "You're welcome! 😊",
    "thanks": "Happy to help!",
    "bye": "Goodbye! Have a great day!",
    "help": """
I can respond to:
- hello
- hi
- hey
- good morning
- good afternoon
- good evening
- how are you
- your name
- ai
- python
- internship
- date
- time
- thank you
- thanks
- bye
- exit
"""
}

print("=" * 50)
print("🤖 Welcome to RuleBot")
print("Project 1 - Rule-Based AI Chatbot")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")
print("=" * 50)

conversation_history = []

while True:

    # Take user input
    user_input = input("\nYou: ").lower().strip()

    # Save user input
    conversation_history.append("You: " + user_input)

    # Exit condition
    if user_input == "exit":
        print("Bot: Thank you for using RuleBot. Goodbye! 👋")
        conversation_history.append("Bot: Session Ended")
        break

    # Date
    elif user_input == "date":
        reply = datetime.datetime.now().strftime("%d-%m-%Y")

    # Time
    elif user_input == "time":
        reply = datetime.datetime.now().strftime("%H:%M:%S")

    # Dictionary Lookup
    else:
        reply = responses.get(
            user_input,
            "Sorry, I don't understand that. Please type 'help' to see available commands."
        )

    # Print response
    print("Bot:", reply)

    # Save response
    conversation_history.append("Bot: " + reply)

# Save conversation
with open("chat_history.txt", "w") as file:
    for line in conversation_history:
        file.write(line + "\n")

print("\nConversation saved successfully as chat_history.txt")