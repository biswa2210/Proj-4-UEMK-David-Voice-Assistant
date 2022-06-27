import speech_recognition as sr


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_Threasold = 1
        audio = r.listen(source,0,4)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='eng-in')
        print(f"You: {query}\n")

    except Exception as e:
        print("Sorry, Can you say that again")
        return "None"
    
    query = str(query)    
    return query.lower()




