
def chatbot():
    print("🤖 CodBot: Hello! I'm CodBot, your assistant.")
    print("📝 Type anything to talk. Type 'bye' to end the chat.\n")

responses = {
        "hi": "Hello there!",
        "hello": "Hi! How can I help you?",
        "hey": "Hey! How’s it going?",
        "how are you": "I'm just a bot, but I'm doing great! 😄",
        "what is your name": "I'm CodBot — your virtual friend.",
        "who are you": "I'm CodBot, created to talk with you and help with tasks.",
        "help": "Sure! You can ask about the internship, projects, or just chat!",
        "what can you do": "I can answer basic questions and guide you during your internship.",
        "thank you": "You're welcome! 😊",
        "thanks": "Happy to help!",
        "bye": "Goodbye! Take care! 👋"
    }

    
    alternate_phrases = {
        "how are you doing": "how are you",
        "what's your name": "what is your name",
        "can you help me": "help",
        "i need help": "help",
        "what do you do": "what can you do",
        "thank you so much": "thank you",
        "thanks a lot": "thanks"
    }

    while True:
        
        user_input = input("You: ").lower().strip()

        
        if user_input in alternate_phrases:
            user_input = alternate_phrases[user_input]

        if user_input == "bye":
            print("🤖 CodBot:", responses["bye"])
            break

        
        elif user_input in responses:
            print("🤖 CodBot:", responses[user_input])

        # If the input is unknown
        else:
            print("🤖 CodBot: Hmm... I don't know how to respond to that yet.")


if __name__ == "__main__":
    chatbot()
