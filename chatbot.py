# A very simple chatbot that replies based on what you type

def chatbot():
    print("🤖 CodBot: Hello! I'm CodBot, your friendly chatbot.")
    print("💬 You can talk to me. Type 'bye' to end the chat.\n")

    # Known questions and their replies
    replies = {
        "hi": "Hi there!",
        "hello": "Hello! How can I help you?",
        "hey": "Hey! What’s up?",
        "how are you": "I'm doing great, thanks for asking! 😄",
        "what is your name": "I'm CodBot. Nice to meet you!",
        "who are you": "I'm a simple chatbot here to help you.",
        "help": "You can ask me things like who I am, what I can do, or just say hi!",
        "what can you do": "I can answer basic questions and chat with you.",
        "thank you": "You're welcome! 😊",
        "thanks": "Anytime!",
        "bye": "Goodbye! Talk to you later. 👋"
    }

    # Similar questions that map to the main ones
    similar_questions = {
        "what's your name": "what is your name",
        "how are you doing": "how are you",
        "can you help me": "help",
        "i need help": "help",
        "what do you do": "what can you do",
        "thank you so much": "thank you",
        "thanks a lot": "thanks"
    }

    # Chat loop
    while True:
        user = input("You: ").lower().strip()

        # Convert similar phrases to main ones
        if user in similar_questions:
            user = similar_questions[user]

        # If the user says bye, end the chat
        if user == "bye":
            print("🤖 CodBot:", replies["bye"])
            break

        # If we know the reply, show it
        elif user in replies:
            print("🤖 CodBot:", replies[user])

        # If we don't understand
        else:
            print("🤖 CodBot: Hmm... I don’t understand that. Try asking something else.")

# Start the chatbot
if __name__ == "__main__":
    chatbot()
