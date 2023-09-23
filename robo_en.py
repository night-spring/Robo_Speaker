#pip install gtts

import gtts

text = input("Enter what you want to say through AI : ")
sound = gtts.gTTS(text, lang="en")
sound.save("english.mp3") 