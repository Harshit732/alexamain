
import webbrowser
import speech_recognition as sr
import pyttsx3
import pyjokes
import pywhatkit
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()


def alexa_talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def main_alexa():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print('\n')
        print("listing")
        rec = r.listen(source)
        try:
            cmd = r.recognize_google(rec, language='en-in')
            cmd = cmd.lower()
            print(cmd)

            if "hello alexa" in cmd:
                alexa_talk('hello i am alexa how can i help you')
            if "hello" in cmd:
                alexa_talk('hello i am alexa how can i help you')
            elif 'what is' in cmd:
                cmd=cmd.replace('what is','')
                info=wikipedia.summary(cmd)
                print(info)
                alexa_talk(info)
            elif 'play' in cmd:
                cmd=cmd.replace('play','')
                pywhatkit.playonyt(cmd)
            elif 'who is' in cmd:
                cmd=cmd.replace('who is','')
                info=wikipedia.summary(cmd)
                print(info)
                alexa_talk(info)
            elif 'search on google' in cmd:
                info= 'http://www.google.com/search?='+cmd.replace('search on google','')
                webbrowser.open(info)
            elif 'find about' in cmd:
                info='http://www.google.cpm/search?q='+cmd.replace('find about','')
                webbrowser.open(info)
            elif 'where is' in cmd:
                cmd=cmd.replace('where is','')
                info='http://google.nl/maps/place/'+cmd+'/&amp'
                webbrowser.open_new(info)
            elif 'locate ' in cmd:
                loc = cmd.replace('locate', '')
                if 'on map' in loc:
                    loc = loc.replace('on map', ' ')
                url = 'https://google.nl/maps/place/' + loc + '/&amp;'
                webbrowser.get().open(url)
                print('Here is the location of ' + loc)
                alexa_talk('Here is the location of ' + loc)
            elif 'on map' in cmd:
                cmd=cmd.replace('on map','')
                if 'find' in cmd:
                    cmd=cmd.replace('find','')
                info='http://google.nl/maps/place/'+loc+'/amp'
                webbrowser.open_new(info)
            elif 'joke' in cmd:
                jokes=pyjokes.get_joke()
                print(jokes)
                alexa_talk(jokes)
            else:
                print(cmd)
                alexa_talk("i can't recognise what you just said")



        except Exception as ex:
            print(ex)


while (True):
    main_alexa()


