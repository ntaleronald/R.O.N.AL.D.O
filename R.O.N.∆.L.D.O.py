import speech_recognition as sr
import webbroswer
import datetime
import os
import time
import subprocess
import wikipedia
import json
import requests
import pyttsx3
import ALEXA


# python to text voice constants
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

# word to respond to to start tasks
WAKE = "Ronaldo"


# function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# go ahead and make a conversation log
CONVERSATION_LOG = ('Conversation log.txt')

SEARCH_WORDS = {'who': 'who', 'what': 'what', 'when': 'when', 'where': 'where', 'why': 'why', 'how': 'how'}


def listen(recognizer, microphone, response):
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            recognizer.dynamic_energy_threshold = 3000
            audio = recognizer.listen(source, timeout=5.0)
            # time it takes to recieve a command, can be increased or reduced
            command = recognizer.recognize_google(audio)
            r.remember(command)
            return command.lower()
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Network Error.")

    # Used to track the date of the conversation, may need to add the time in the future


class Ronaldo:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    # used to hear the commands and initiate greeting

    def start_conversation_log(self):
        today = str(datetime.date.today())
        today = today
        with open(CONVERSATION_LOG, "a") as f:
            f.write("Conversation started on: " + today + "\n")

        # Writes each command from the user to the conversation log

    def remember(self, command):
        with open(CONVERSATION_LOG, "a") as f:
            f.write("User: " + command + "\n")

    # checks the first word in the command to determine if its a search word
    def find_search_words(self, command):
        if SEARCH_WORDS.get(command.split('')[0]) == command.split('')[0]:
            return True

    # analyzes the command
    def analyze(self, command):
        try:
            if self.find_search_words(command):
                speak('Here is what I found.')
                webbroswer.open("http://www.google.com/search?q={}".format(command))
            elif command == "open youtube.":
                speak('Opening Youtube')
                print('Opening youtube')
                webbroswer.open('https://www.youtube.com')
            elif command == 'introduce yourself':
                speak('I am Ronaldo, your virtual assitant')
            elif command == 'wikipedia':
                command = command.replace('wikipedia', '')
                results = wikipedia.summary(command, sentences=3)
                speak('According to Wikipedia')
                print(results)
                speak(results)
            elif command == 'open gmail':
                speak('Opening gmail')
                webbroswer.open('gmail.com')
            elif command == 'open instagram':
                speak('opening instagram')
                webbroswer.open('www.instagram.com')
            elif command == 'open stack over flow':
                speak('Opening stack over flow')
                webbroswer.open('stackoverflow.com')
            elif command == 'news':
                news = webbroswer.open('editon.cnn.com')
                speak('Here is the latest news')
            elif 'who are you' in command or 'what can you do' in command:
                speak('I am G-one version 1 point O your personal assistant. I am programmed to minor tasks like'
                      'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                      'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
            elif "who made you" in command or "who created you" in command or "who discovered you" in command:
                speak("I was built by Ronaldo")
                print("I was built by Ronaldo")
            elif "weather" in command:
                api_key = "Apply your unique ID"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("what is the city name")
                city_name = command()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

            elif "log off" in command or "sign out" in command:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
                time.sleep(3)
            else:
                speak('I do not know how to do that yet')
        except TypeError:
            pass

    # used to listen for wake word
    def hear(self, recognizer, microphone):
        while True:
            try:
                with microphone as source:
                    print('Listening...')
                    recognizer.adjust_for_ambient_noise(source)
                    recognizer.dynamic_energy_threshold = 3000
                    audio = recognizer.listen(source, timeout=5.0)
                    response = recognizer.recognize_google(audio)
                    if response == WAKE:
                        hour = datetime.datetime.now().hour
                        if hour >= 0 and hour <= 12:
                            speak("Hello, Good morning")
                            print("Hello, Good morning")
                        elif hour >= 12 and hour <= 18:
                            speak('Hello there, Good Afternoon')
                            print('Hello there, Good Afternoon')
                        else:
                            speak('Salutaions, Lovely Evening we are having, innit')
                            print('Salutaions, Lovely Evening we are having, innit')
                        return response.lower()
                    else:
                        pass
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print('Network error')


r = Ronaldo
r.start_conversation_log()

run_alexa = ALEXA
while True:
    r()
