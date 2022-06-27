import pywhatkit
from say import speak,speakAF
from Listen import  takeCommand
from math import factorial








def addition():
    try:
        print("How many numbers you want to add")
        speakAF("How many numbers you want to add")
        n = takeCommand()
        i=1
        sum=0
        while(i<=int(n)):
            print("Tell me the number" +" "+ str(i))
            speakAF("Tell me the number"+str(i))
            var=takeCommand()
            sum= sum + int(var)
            i=i+1
        print("Sum of the numbers is" +" "+ str(sum))
        speakAF("Sum of the numbers is"+ str(sum))
    except Exception as e:
        print("Sorry I did not understand ")
        speakAF("Sorry I did not understand")
        addition()


def substraction():
    try:
        print("Tell me the 1st number")
        speakAF("Tell me the 1st number")
        var1=takeCommand()

        print("Tell me the 2nd number")
        speakAF("Tell me the 2nd number")
        var2 = takeCommand()

        sub=int(var1)-int(var2)

        print("Substraction of the numbers is" +" "+ str(sub))
        speakAF("Substraction of the numbers is"+ str(sub))
    except Exception as e:
        print("Sorry I did not understand ")
        speakAF("Sorry I did not understand")
        substraction()


def division():
    try:
        print("Tell me the 1st number")
        speakAF("Tell me the 1st number")
        var1=takeCommand()

        print("Tell me the 2nd number")
        speakAF("Tell me the 2nd number")
        var2 = takeCommand()

        div=int(var1)/int(var2)

        print("Substraction of the numbers is" +" "+ str(div))
        speakAF("Substraction of the numbers is"+ str(div))
    except Exception as e:
        print("Sorry I did not understand ")
        speakAF("Sorry I did not understand")
        division()


def multiplication():
    try:
        print("How many numbers you want to multiply")
        speakAF("How many numbers you want to multiply")
        n = takeCommand()
        i=1
        mul=1
        while(i<=int(n)):
            print("Tell me the number" +" "+ str(i))
            speakAF("Tell me the number"+str(i))
            var=takeCommand()
            mul= mul * int(var)
            i=i+1
        print("multiplication of the numbers is" +" "+ str(mul))
        speakAF("multiplication of the numbers is"+ str(mul))
    except Exception as e:
        print("Sorry I did not understand ")
        speakAF("Sorry I did not understand")
        multiplication()


def pascaltriangle():
    try:
        print("Tell me the no. of rows for the triangle")
        speakAF("Tell me the no. of rows for the triangle")
        n = takeCommand()
        n = int(n)
        for i in range(n):
            for j in range(n - i + 1):
                # for left spacing
                print(end=" ")

            for j in range(i + 1):
                # nCr = n!/((n-r)!*r!)
                print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
            print()
    except Exception as e:
        print("Sorry I did not understand ")
        speakAF("Sorry I did not understand")
        pascaltriangle()

