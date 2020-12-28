import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices: object = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_task():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            task = listener.recognize_google(voice)
            task = task.lower()
            if 'alexa' in task:
                task = task.replace('alexa', '')
                print(task)
    except:
        pass
    return task


def run_alexa():
    task = take_task()
    print(task)
    if 'play' in task:
        song = task.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in task:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in task:
        person = task.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in task:
        talk('sorry, I have a headache')
    elif 'are you single' in task:
        talk('I am in a relationship with wifi')
    elif 'joke' in task:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
