from gtts import gTTS
import os


# It's just a text to speech function..
def saySomething(somethingToSay):
    myobj = gTTS(text=somethingToSay, lang="es", slow=False)
    myobj.save("somethingToSay.mp3")
    os.system("mpg321 somethingToSay.mp3")


while True:
    something = input("Something to say? ")
    print("Saying something with speakers..")
    saySomething(something)