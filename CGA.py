import pywhatkit
from say import speakNCS
def controlGoogleAutomation(ans,statement):
    if ans == "yes":
        if statement=="Amstrong Number":
            pywhatkit.search("Amstrong number")
        elif statement=="Happy Number":
            pywhatkit.search("Happy number")
    elif ans == "no":
        speakNCS("ok,no  problem")
    else:
        speakNCS("Sorry,I can't recognize your answer properly")