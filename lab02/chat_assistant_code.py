import random

# A simple themed chat assistant example
class ChatAssistant:
    def __init__(self, theme):
        self.theme = theme
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What would you like to talk about?"],
            "topic": ["Let's talk about {}.", "I'm interested in {} too."],
            "farewell": ["Goodbye! Have a great day!", "See you later!"]
        }
    
    def get_response(self, user_input):
        if "hello" in user_input.lower():
            return random.choice(self.responses["greeting"])
        elif "bye" in user_input.lower():
            return random.choice(self.responses["farewell"])
        else:
            return random.choice(self.responses["topic"]).format(self.theme)

# Example usage
if __name__ == "__main__":
    theme = "space exploration"
    assistant = ChatAssistant(theme)
    print("Chat Assistant Ready! Type your message.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = assistant.get_response(user_input)
        print("Assistant: ", response)