# CodeAgent: Develop the chat assistant tailored to a specific theme, such as a mental health support bot.
import openai

class ChatAssistant:
    def __init__(self):
        self.topic = 'Mental Health Support'

    def generate_response(self, user_input):
        prompt = f"You are a helpful assistant specialized in {self.topic}. User input: {user_input}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']

    def run(self):
        print("Welcome to the Mental Health Support Chat Assistant")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                break
            answer = self.generate_response(user_input)
            print("Assistant: ", answer)

# Instantiate and run the assistant
if __name__ == "__main__":
    assistant = ChatAssistant()
    assistant.run()