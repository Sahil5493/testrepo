import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import pyjokes
import pyttsx3
from AppOpener import run
import os
import pywhatkit
import datetime
import webbrowser
import os
# import controller as ctr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id )
engine.setProperty('rate', 200)

url = 'https://www.google.com/search?q='

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak('good morning sahil')

    elif hour >=12 and hour<18:
        speak("good afternoon")

    else:
        speak('good evening')

    speak("Jarvis here. Please tell me how can i help you")
    
def exit():
    speak('Thank you and have a nice day')
# def goodnight():
#     speak('Good night Sahil have a sweet dreams!')


def takeCommand():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            # query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            # speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif 'joke' in query:
            speak('Recognizing jokes')
            joke = pyjokes.get_joke(language = 'en', category = "all")
            speak(joke)
        
        elif 'music' in query:
            music_dir = 'D:\\Movies'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[1]))
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {strTime}")
            print(strTime)
            
        elif 'code' in query:
            vsPath = '"D:\Microsoft VS Code\Code.exe"'
            os.startfile(vsPath)
            
        if 'calculator' in query:
                    speak('opening calculator')
                    run('calculator')

        elif 'chrome' in query:
                    speak('opening chrome')
                    run('google chrome')

        elif 'shutdown' in query:
                    speak('shuttingdown')
                    os.system('shutdown /s /t')
                
        elif 'restart' in query:
                    speak('restarting pc')
                    os.system('shutdown /r /t')

        elif 'song' in query:
                    speak('which song you would like to listen')
                    takeCommand()
                    pywhatkit.playonyt(query)

        elif 'send message' in query:
                    speak('sending message')
                    pywhatkit.sendwhatmsg("+919601511339", "Hi", 19, 12)

        elif 'Google' in query:
                    speak('what you want to search')
                    a = takeCommand()
                    search_url = url + a
                    webbrowser.open(search_url)

        # elif 'Bluetooth' in query:
        #             os.system("sudo hciconfig hci0 up")
        #             speak("Bluetooth is turned on")
        # elif 'Close Bluetooth' in query:
        #             os.system("sudo hciconfig hci0 up")
        #             print("Bluetooth is turned off")
            

        # elif 'turn on' in query:
        #     speak('Turning on light')
        #     ctr.led(1)
        # elif 'turn off' in query:
        #     speak('Turning off light')
        #     ctr.led(0)
            
            
        elif 'exit' in query:
            break
            
        else: 
            speak('could not recognize your voice!')
            
    exit()
            
    
