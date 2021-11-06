from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os

def play(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("texttospeech.mp3")
    os.system("texttospeech.mp3")
    os.remove("./texttospeech.mp3")
