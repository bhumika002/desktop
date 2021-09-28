import pyttsx3  # pyttsx3 is a text-to-speech conversion library
# The requests module allows you to send HTTP requests using Python.
import requests
from requests.api import head
from urllib.request import Request
import speech_recognition as sr  # for converting spoken words to text
import datetime  # supplies classes for manipulating dates and times
import os  # provides functions for interacting with the operating system
import cv2  # bindings designed to solve computer vision problems
# import random
from requests import get
import wikipedia  # makes it easy to access and parse data from Wikipedia
import webbrowser  # which allows to open the web browser
import pywhatkit as kit  # for Sending whatsapp message at certain time
import smtplib  # which defines an SMTP client session object that can be used to send mail to any       Internet machine
import pyjokes  # used to actually return a single joke from a certain category and in a particular language
# provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
import sys
import time
import pyautogui  # that allows you to control the mouse and keyboard to do various things


# To convert text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices)-1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# To wish


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%p")

    if hour >= 0 and hour <= 12:
        speak(f"Good morning!,it's {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good afternoon!,it's {tt}")
    else:
        speak(f"Good evening!,it's {tt}")

    speak("I am Ultron   Mam Please tell me how can i help you")

# to send email


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jayarawat.2903@gmail.com', 'password')
    server.sendmail('jayarawat.2903@gmail.com', to, content)
    server.close()

# For news update


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e878276ac8b34661ae856e6db29e259a'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's{day[i]} news is:{head[i]}")


if __name__ == "__main__":
    wish()
    while True:
        # if 1:
        query = takeCommand().lower()

        # logic building for task

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open vs code " in query:
            bpath = "C:\\Users\\hi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "C:\\Users\\hi\\Music\\Favorite Songs2"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")

        elif "open google" in query:
            speak("Mam,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+918959200691",
                            "anything you want to send in msg", 1, 31)
            time.sleep(120)
            speak("message has been send")

        elif "play song on youtube" in query:
            kit.playonyt("lagi meri tere sang lagi")

            # print(e)
            # speak("Sorry mam, i am not able to sent this mail to neha")

        elif "you can sleep" in query:
            speak("thanks for using me mam,have a good day")
            sys.exit()

        # To close any application
        elif "close notepad" in query:
            speak("okay mam,closing notepad")
            os.system("taskkill/f /im notepad.exe")

        elif "close vs code" in query:
            speak("okay mam,closing notepad")
            os.system("taskkill/f /im Code.exe")

        elif "close command prompt " in query:
            speak("okay mam,closing notepad")
            os.system("taskkill/f /im cmd.exe")

        elif "close camera" in query:
            speak("okay mam,closing notepad")
            os.system("taskkill/f /im camers.exe")

        elif "close google chrome" in query:
            speak("okay mam,closing notepad")
            os.system("taskkill/f /im chrome.exe")

        elif "close adobe reader" in query:
            speak("okay mam,closing adobe reader")
            os.system("taskkill/f /im  AcroRd32.exe")

        # To set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 19:
                music_dir = 'C:\\Users\\hi\\Music\\Favorite Songs2'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        # To find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown/s /r /t 5")

        elif "restart the system" in query:
            os.system("shutdown/r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait mam,fetching the latest news")
            news()

        elif "send email to neha" in query:
            try:
                speak("what should i say?")
                content = takeCommand().lower()
                to = "neharawat1306@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to neha")
            except Exception as e:
                print(e)
                speak("Sorry mam, i am not able to sent this mail to neha")
