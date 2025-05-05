import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Theme-specific assistant: Travel Guide
@api.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'You are a helpful travel guide.'},
            {'role': 'user', 'content': user_input}
        ]
    )
    answer = response.choices[0].message['content']
    return jsonify({'reply': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)