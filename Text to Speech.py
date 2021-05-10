def TTS_():
    import pyttsx3
    engine = pyttsx3.init()
    nandu = input('Text To Speech - Enter Text : ')
    engine.say(nandu)
    engine.runAndWait()
    
while True:
    TTS_()
    if input() == "exit" or "quit":
        break
