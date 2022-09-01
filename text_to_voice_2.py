##TTS dependencis##
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound


##TTS code##
def speak(text):

     tts = gTTS(text=text, lang='ko', slow=False)
     filename='answer.mp3'
     tts.save(filename)
     playsound.playsound(filename)

speak('안녕하세요')