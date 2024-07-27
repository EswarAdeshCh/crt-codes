"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyD5KMn0G0uU_8Ayu2rb0XKvlzAz-bkEPsM")


# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel( 
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction= "your name is spidey,you are actually spiderman",
)

chat_session = model.start_chat(
    history=[
    ]
)

while True:
    user_input = input("Enter your message (type 'stop' to end): ")
    if user_input.lower() == "stop":
        print("Stopping the chat session.")
        break

    response = chat_session.send_message(user_input)
    print("AI Response:", response.text)