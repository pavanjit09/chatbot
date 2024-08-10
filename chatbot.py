def chatbot():
    print("Hello! I am a simple chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        elif user_input in ['hi', 'hello']:
            print("Chatbot: Hello! How can I assist you today?")
        elif user_input in ['how are you', 'how are you?']:
            print("Chatbot: I'm just a program, but I'm doing well. How can I help you?")
        elif user_input in ['what is your name?', 'what is your name']:
            print("Chatbot: I am a chatbot created by an AI developer.")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()

