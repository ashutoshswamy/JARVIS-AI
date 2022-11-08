import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# In wishMe() function instead of Mr. Swamy you can set your own name


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Hello Mr. Swamy, Good Morning!")
        speak("Hello Mr. Swamy, Good Morning!")

    elif hour >= 12 and hour < 18:
        print("Hello Mr. Swamy, Good Afternoon!")
        speak("Hello Mr. Swamy, Good Afternoon!")

    else:
        print("Hello Mr. Swamy, Good Evening!")
        speak("Hello Mr. Swamy, Good Evening!")

    print("I am JARVIS Sir, please tell me how may I help you?")
    speak("I am JARVIS Sir, please tell me how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            link = wikipedia.page(query)
            speak("According to Wikipedia")
            print(f"\n{results}")
            speak(results)
            print(f"For more info go to - {link.url}")
            speak(f"For more info go to - {link.url}")
        elif "open google" in query:
            print("\nOpened Google")
            speak("Opened Google")
            webbrowser.open("https://google.com")
        elif "open youtube" in query:
            print("\nOpened YouTube")
            speak("Opened YouTube")
            webbrowser.open("https://youtube.com")
        elif "open instagram" in query:
            print("\nOpened Instagram")
            speak("Opened Instagram")
            webbrowser.open("https://instagram.com")
        elif "open twitter" in query:
            print("\nOpened Twitter")
            speak("Opened Twitter")
            webbrowser.open("https://twitter.com")
        elif "open reddit" in query:
            print("\nOpened Reddit")
            speak("Opened Reddit")
            webbrowser.open("https://reddit.com")
        elif "open pinterest" in query:
            print("\nOpened Pinterest")
            speak("Opened Pinterest")
            webbrowser.open("https://pinterest.com")
        elif "open github" in query:
            print("\nOpened GitHub")
            speak("Opened GitHub")
            webbrowser.open("https://github.com")
        elif "open netlify" in query:
            print("\nOpened Netlify")
            speak("Opened Netlify")
            webbrowser.open("https://netlify.com")
        elif "open discord" in query or "open dc" in query:
            # Paste Discord's path which is in your system
            path = "C:\\Users\\HP\\AppData\\Local\\Discord\\app-1.0.9007\\Discord.exe"
            os.startfile(filepath=path)
            print("\nOpened Discord")
            speak("Opened Discord")
        elif "open vs code" in query or "open code" in query:
            # Paste the VS Code's path which is in your system
            path = (
                "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            )
            os.startfile(filepath=path)
            print("\nOpened Visual Studio Code")
            speak("Opened Visual Studio Code")
        elif "open pycharm" in query or "open python ide" in query:
            # Paste the PyCharm's path which is in your system
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.1\\bin\\pycharm64.exe"
            os.startfile(filepath=path)
            print("\nOpened PyCharm")
            speak("Opened PyCharm")
        elif (
            "open intelli j" in query
            or "open intellij" in query
            or "open java ide" in query
        ):
            # Paste the IntelliJ's path which is in your system
            path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.2.1\\bin\\idea64.exe"
            os.startfile(filepath=path)
            print("\nOpened IntelliJ")
            speak("Opened IntelliJ")
        elif "date" in query:
            date = datetime.datetime
            final_date = date.date()
            print(f"\nSir, today's date is {final_date}")
            speak("Sir, today's date is {final_date}")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"\nSir, the time right now is {strTime}")
            speak(f"Sir, the time right now is {strTime}")
        elif "exit" in query:
            print("\nYou can call me again at any time, Bye Sir")
            speak("You can call me again at any time, Bye Sir")
            exit()
