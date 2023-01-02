import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init()

# jarvis voice setup
voices = engine.getProperty("voices")
voice = engine.setProperty("voice", voices[1].id)


def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Good morning Mam how may i help you ")
        speak("Good morning Mam how may i help you ")
    elif hour >= 12 and hour < 16:
        print("Good AfterNoon  Mam how may i help you ")
        speak("Good AfterNoon  Mam how may i help you ")
    else:
        print("Good Evening  Mam how may i help you ")
        speak("Good Evening  Mam how may i help you ")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# function for listening voice and give us result of this voice by write
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.energy_threshold = 2500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="eng-pak")
        print(f"You Says {query}")
        speak(f"You Says {query}")

    except Exception as e:
        print("please say again")
        return None
    return query
if __name__ == '__main__':

    wish_me()
    while True:
       query=take_command().lower()
       if "Google" in query:
        webbrowser.open("google.com")
       if "wikipedia" in query:
           print("Searching... ")
           speak("Searching")
           result=wikipedia.summary(query,sentences=1)
           speak("According To Wikipedia")
           print(result,end=",")
           speak(result)

       elif "youtube" in query:
           webbrowser.open("youtube.com")
       elif "hello" in query:
           speak("hello how are you !")
       elif "fine" or "ok" or "good" in query:
           speak("Thats Good")
       elif "facebook" in query:
           webbrowser.open("facebook.com")
       elif "search" in query:
           query=query.replace("search"," ")
           pywhatkit.search(query)
       elif "songs" or "music" in query:
           pywhatkit.playonyt(query)
           




