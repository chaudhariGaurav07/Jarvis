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
    speak("heyy mihir how are you")