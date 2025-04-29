responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "what is your name": "you can call me your virtual assistant",
    "help": "You can say hello, ask how I am, or say bye."
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    return responses.get(user_input, "Sorry, I don't understand that.")

def store_conversation(conversation):
    with open("conversation_log.txt", "a") as file:
        for entry in conversation:
            file.write(entry + "\n")

def chatbot():
    print("Welcome to Mini Chatbot! (type 'bye' to exit)")
    conversation = []
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)      
        
        conversation.append(f"You: {user_input}")
        conversation.append(f"Bot: {response}")
        
        if user_input.lower().strip() == "bye":
            break

    store_conversation(conversation)
    print("Conversation saved. Goodbye!")

chatbot()