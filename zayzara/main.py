import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)

print("Welcome to Zayzara Speaker created by Shanzay Khan")

while True:
    x = input("Enter what you want me to speak: ")

    if x.lower() == "q":
        engine.say("Bye bye friend")
        engine.runAndWait()
        break

    engine.say(x)
    engine.runAndWait()
