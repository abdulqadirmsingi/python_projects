from gtts import gTTS
import os

mytext = "hud is a student from UDSM and he studies computer science"
audio = gTTS(text=mytext, lang="en", slow=False)

audio.save("example.mp3")
os.system("start example.mp3")