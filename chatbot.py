def chatbot():
    print("🤖 Chatbot: Hi! I am CodBot. Type 'bye' to end the chat.")

    # Predefined rules using dictionary
    responses = {
        "hi": "Hello there!",
        "hello": "Hi! How can I help you?",
        "how are you": "I'm an AI, but I'm doing great! Thanks for asking.",
        "what is your name": "I'm CodBot, your virtual assistant.",
        "help": "Sure! You can ask me about the internship, tasks, or anything else.",
        "bye": "Goodbye! Have a nice day.",
    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("🤖 Chatbot:", responses["bye"])
            break
        elif user_input in responses:
            print("🤖 Chatbot:", responses[user_input])
        else:
            print("🤖 Chatbot: I'm sorry, I didn't understand that. Can you try something else?")

# Run the chatbot
chatbot()
