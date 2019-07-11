import speech_recognition as sr
import os
os.chdir('F:\\personal project\\speech recognition')
#print(sr.__version__)
r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
mic=sr.Microphone()



with mic as source:
   # r.adjust_for_ambient_noise(source)
    r.adjust_for_ambient_noise(source)
    audio1=r.listen(source)
    #audio2=r.record(source,duration=4)

text1=r.recognize_google(audio1)
#text2=r.recognize_google(audio2)
print(text1)
#print(text2)
