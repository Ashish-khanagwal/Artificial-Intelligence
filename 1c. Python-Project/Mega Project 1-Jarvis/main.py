import os
import webbrowser

import musiclibrary
import pygame
import pyttsx3
import requests
import speech_recognition as sr
from config import api_key, newsapi
from gtts import gTTS
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def aiProcessPerplexity(command):
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.perplexity.ai",  # Pointing to Perplexity's API endpoint
    )

    completion = client.chat.completions.create(
        model="sonar-pro",  # or "sonar-medium-online" etc. depending on your use case
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please",
            },
            {"role": "user", "content": command},
        ],
        max_tokens=500,
        temperature=0.7,
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article["title"])

    else:
        output = aiProcessPerplexity(c)
        speak(output)


if __name__ == "__main__":
    speak("At your service, sir.")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yea")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error; {e}")

