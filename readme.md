# Wishy WhatsApp Bot

Wishy is a WhatsApp bot for community MLSA that allows users to interact with ChatGPT and receive push notifications. This bot is built using Python, Flask, Twilio, and the OpenAI API.

## Features

ChatGPT integration: Users can type questions and get answers from ChatGPT.
Push notifications (not implemented): Future implementation to allow sending community updates.

## Prerequisites

Python 3
A Twilio account with WhatsApp Sandbox activated
An OpenAI API key

## Installation

Clone this repository or download it as a ZIP file.
Navigate to the project folder in your terminal or command prompt.
(Recommended) Create a virtual environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required libraries:
bash
Copy code
pip install twilio flask openai
Open app.py in a text editor and replace your_openai_api_key with your actual OpenAI API key.

## Usage

Run the Flask application:
`python app.py`
In a separate terminal or command prompt, run ngrok to expose your local server:

`./ngrok http 5000  # On Windows, use ngrok.exe http 5000`

Copy the https:// URL provided by ngrok.

Go to your Twilio WhatsApp Sandbox `(https://www.twilio.com/console/sms/whatsapp/sandbox)` and enter the ngrok URL, followed by the /bot endpoint, into the "When a message comes in" field:
plaintext
`https://your-ngrok-subdomain.ngrok.io/bot`
Click "Save" to update your webhook settings.
Follow the instructions in the Twilio Console to join the sandbox, then send a message to the provided WhatsApp number to test the bot.

### Limitations and Future Work

The current implementation does not include push notifications. This feature requires a more complex architecture, such as using Firebase or another service to handle notifications and user data.
The bot is running on a free Twilio account, which has limited features and usage. It may not be suitable for large-scale deployments.

### License

This project is provided under the MIT License. See the LICENSE file for more information.
