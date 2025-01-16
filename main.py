import speech_recognition as sr
import sys
rec = sr.Recognizer()
with sr.Microphone() as srm:
    while True:
       print("Say Somtheing...")
       audio = rec.listen(srm)
       text = rec.recognize_google(audio)
       
       if text in "Hello":
         print("How are you?")
       elif text in ["Good", "Good, Thanks", "Not Good", "Good And You"]:
         print("Nice To meet You")
       elif text in "Close Chat":
        sys.exit(0)
       else:
         print("I didn't understand you well")