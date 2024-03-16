import os
import openai
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer {api-key}"}

load_dotenv()
openai.api_key = ''
model = 'gpt-3.5-turbo'
# Set up the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
name = "YOUR NAME HERE"
greetings = [f"greetings {name}",
             "hola",
             "Hey there, how's it going today?",
             f"Hello, how's your day going so far?"]


def listen_for_wake_word(source):
    print("Listening for 'Hello'...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "hello" in text.lower():
                print("Wake word detected.")
                engine.say(np.random.choice(greetings))
                engine.runAndWait()
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass


# Listen for input and respond with OpenAI API
def listen_and_respond(source):
    print("Listening...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if not text:
                continue
            if "describe image" in text.lower():
                print("Describing image")
                desc = query()
                engine.say(desc)
                engine.runAndWait()
                listen_and_respond(source)

            # Send input to OpenAI API
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=[{"role": "user", "content": f"{text}"}])
            response_text = response.choices[0].message.content
            print(f"OpenAI response: {response_text}")

            # Speak the response
            engine.say(response_text)
            engine.runAndWait()

            if not audio:
                listen_for_wake_word(source)
        except sr.UnknownValueError:
            time.sleep(2)
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            engine.say(f"Could not request results; {e}")
            engine.runAndWait()
            listen_for_wake_word(source)
            break


image_url = "http://192.168.0.100/640x480.jpg" #This is the url of esp32 cam
def query():
    # Retrieve the image data from the URL
    image_data = requests.get(image_url).content
    response = requests.post(API_URL, headers=headers, data=image_data)
    output = response.json()
    description = output[0]['generated_text']
    print(description)
    return description


# Use the default microphone as the audio source
with sr.Microphone() as source:
    listen_for_wake_word(source)




