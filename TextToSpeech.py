# from gtts import gTTS
import pyttsx3
import random
# import os

def play():
    engine = pyttsx3.init()

    with open('pickup_lines.txt') as file:
        lines = file.readlines()

    rand_int = random.randrange(1, len(lines))
    print(lines[rand_int])
    # engine.say(lines[rand_int])
    engine.say(lines[rand_int])
    engine.runAndWait()
    # language = 'en'
    # myobj = gTTS(text=mytext, lang=language, slow=False)
    # myobj.save("texttospeech.mp3")
    # os.system("texttospeech.mp3")
    # os.remove("./texttospeech.mp3")


play()
