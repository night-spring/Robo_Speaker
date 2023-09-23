#pip install gtts
#pip install playsound

import gtts
from playsound import playsound

text = input("Enter what you want to say through AI : ")
sound = gtts.gTTS(text, lang="en")
sound.save("english.mp3") 
playsound("english.mp3")
