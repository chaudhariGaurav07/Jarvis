import speech_recognition as sr
#for rendering through web browser 
import webbrowser 
#used for text to speech 
import pyttsx3  

#recognizer it is class that provide the speech recognition functinality
recognizer = sr.Recognizer()
engine = pyttsx3.init() #initialization

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Initializing Jarvis..")
    while True:
        # listen for the wake uo word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as sourse:
            print("Listening...")
            audio = r.listen(sourse)

    

        # recognize speech using google speech 
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("google could not understand audio")
        except sr.RequestError as e:
            print("google error; {0}".format(e))