import random

# Dictionary of predefined responses
responses = {
    "greetings": ["Hello! How can I assist you today?", "Hi there! How may I help you?", "Welcome! How can I assist you?"],
    "product_inquiry": ["Sure! Our products are of top quality. What are you looking for?", "We have a wide range of products. What specific item are you interested in?", "I can help you find the perfect product. What type of item are you searching for?"],
    "order_status": ["To check your order status, please provide your order number.", "Sure! I can assist you with your order. Please provide your order number.", "To help you with your order, I'll need your order number."],
    "thanks": ["You're welcome! If you have any more questions, feel free to ask.", "No problem! If there's anything else I can assist you with, just let me know.", "You're welcome! Have a great day!"],
    "fallback": ["I'm sorry, I didn't quite understand. Could you please rephrase?", "Apologies, but I couldn't comprehend that. Can you please provide more information?", "I'm sorry, I'm not sure I follow. Can you please clarify?"],
}

# Function to generate bot responses
def generate_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greetings"])
    elif "product" in user_input or "item" in user_input:
        return random.choice(responses["product_inquiry"])
    elif "order" in user_input or "status" in user_input:
        return random.choice(responses["order_status"])
    elif "thanks" in user_input or "thank you" in user_input:
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["fallback"])

# Main loop for chat interaction
def chat():
    print("Welcome to the e-commerce chatbot!")
    print("How can I assist you today?")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        bot_response = generate_response(user_input)
        print("Bot:", bot_response)

# Start the chatbot
chat()
