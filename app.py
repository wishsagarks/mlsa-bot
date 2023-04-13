import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

openai.api_key = "your_openai_api_key"

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'push notification' in incoming_msg:
        # Your push notification logic here
        msg.body("Push notification is not yet implemented.")
    elif 'chatgpt' in incoming_msg:
        # Your ChatGPT API logic
        question = incoming_msg.replace("chatgpt", "").strip()
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{question}",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        msg.body(f"Answer: {answer}")
    else:
        msg.body("Welcome to Wishy! Please choose an option:\n1. Push notification\n2. ChatGPT API")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
