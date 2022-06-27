import pywhatkit
from say import speak,speakNCS
from Listen import  takeCommand
from NCS_2_HELPER import power,order,digitsquaresum,digitsum,reversenum,isprimeno
from CGA import controlGoogleAutomation

def amstrong(no):
    #------------LOGIC-------------#
    n = order(no)
    temp = no
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

    # If condition satisfies
    if (sum1 == no):
        speak("It is Amstrong Number")
    else:
        speak("It is not Amstrong Number")
    # ------------LOGIC-------------#

    speakNCS("An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself")
    speakNCS("do you want to know more about Amstrong numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans,"Amstrong Number")

def happyno(no):
    # ------------LOGIC-------------#
   if(no>9):
       while(no>9):
           no=digitsquaresum(no)
       if(no==1):
           speak("It is Happy Number")
       else:
           speak("It is not Happy Number")

   elif(no==1):
       speak("It is Happy Number")

   else:
       speak("It is not Happy Number")
    # ------------LOGIC---------------#

   speakNCS("A number is called happy if it leads to 1 after a sequence of steps wherein each step number is replaced by the sum of squares of its digit that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1. ")
   speakNCS("do you want to know more about Happy numbers ?")
   speakNCS("please say yes or no")
   ans = takeCommand()
   controlGoogleAutomation(ans, "Happy Number")


def magic(no):
    # ------------LOGIC-------------#
   if(no>9):
       while(no>9):
           no=digitsum(no)
       if(no==1):
           speak("It is Magic Number")
       else:
           speak("It is not Magic Number")

   elif(no==1):
       speak("It is Magic Number")

   else:
       speak("It is not Magic Number")
    # ------------LOGIC---------------#

   speakNCS("A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1,then the number is a magic number. ")
   speakNCS("do you want to know more about Magic numbers ?")
   speakNCS("please say yes or no")
   ans = takeCommand()
   controlGoogleAutomation(ans, "Magic Number")


def perfect(no):
    # ------------LOGIC-------------#
   sum=0
   i=1
   while(i<no):
       if(no%i==0):
           sum=sum+i
       i=i+1
   if(sum==no):
        speak("It is Perfect Number")
   else:
        speak("It is not perfect Number")
    # ------------LOGIC---------------#

   speakNCS("A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. Write a function to check if a given number is perfect or not. ")
   speakNCS("do you want to know more about Magic numbers ?")
   speakNCS("please say yes or no")
   ans = takeCommand()
   controlGoogleAutomation(ans, "Perfect Number")


def palindrome(no):
    # ------------LOGIC-------------#
   temp=no
   no=reversenum(no)
   if(temp==no):
        speak("It is Palindrome Number")
   else:
        speak("It is not Palindrome Number")
    # ------------LOGIC---------------#

   speakNCS("A palindrome is a number that remains the same even if the number is inverted.")
   speakNCS("do you want to know more about Palindrome numbers ?")
   speakNCS("please say yes or no")
   ans = takeCommand()
   controlGoogleAutomation(ans, "Palindrome Number")

def smith(no):
    # ------------LOGIC---------------#
    prime_factors = []
    temp = no
    c = 2
    while (temp > 1):
        if (temp % c == 0 and isprimeno(c)):
            prime_factors.append(c)
            temp /= c
        else:
            c += 1
            continue
    for i in range(0, len(prime_factors)):
        if (order(prime_factors[i]) > 1):
            while (order(prime_factors[i]) > 1):
                prime_factors[i] = digitsum(prime_factors[i])
    if (sum(prime_factors) == digitsum(no)):
        speak("It is Smith Number")
    else:
        speak("It is not Smith Number")
    # ------------LOGIC---------------#

    speakNCS("A Smith Number is a composite number whose sum of digits is equal to the sum of digits in its prime factorization.")
    speakNCS("do you want to know more about smith numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Smith Number")

def duck(no):
    #-------------LOGIC--------------#
    no = str(no)
    no = no.lstrip("0")
    if ("0" in no):
        speak("It is Duck Number")
    else:
        speak("It is not Duck Number")
    #------------LOGIC--------------#

    speakNCS("If given number has zero in between or end, that is called Duck number.")
    speakNCS("do you want to know more about duck numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans,"Duck Number")


def strong(no):
    # -------------LOGIC--------------#
    sum = 0
    temp = no
    while (no):
        i = 1
        fact = 1
        rem = no % 10
        while (i <= rem):
            fact = fact * i  # Find factorial of each number
            i = i + 1
        sum = sum + fact
        no = no // 10
    if (sum == temp):
        speak("It is a strong number")
    else:
        speak("It is not a strong number")
        # ------------LOGIC--------------#

    speakNCS("A Strong number is a special number whose sum of the all digit factorial should be equal to the number itself.")
    speakNCS("do you want to know more about strong numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Strong Number")

def composite(no):
    #-------------LOGIC--------------#
    count = 0
    for a in range(2, no):
        if no % a == 0:
            count += 1
    if count >= 1:
        speak("It is Composite Number")
    else:
        speak("It is not Composite Number because It is prime number")
    #------------LOGIC--------------#

    speakNCS("Composite number is a whole numbers that have on 1 or more than 1 factors excluding 1 and itself. ")
    speakNCS("do you want to know more about composite numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans,"Composite Number")


def harshad(no):
    #-------------LOGIC--------------#
    copy = no
    digit_sum = 0

    while no:
        digit_sum += no % 10
        no //= 10

    if copy % digit_sum == 0:
        speak('It is Harshad Number')
    else:
        speak('It is not Harshad Number')
    #------------LOGIC--------------#

    speakNCS("a number is said to be Harshad number if it is divisible by the sum of its digits.")
    speakNCS("do you want to know more about harshad numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans,"Harshad Number")






def notRecogCheck(var,statement):
    if var is not "None":
        no = int(var)
        print("Input :: " + str(no))
        if statement=="amstrong":
            amstrong(no)
        elif statement=="happy":
            happyno(no)
        elif statement=="magic":
            magic(no)
        elif statement=="perfect":
            perfect(no)
        elif statement=="palindrome":
            palindrome(no)
        elif statement=="smith":
            smith(no)
        elif statement=="duck":
            duck(no)
        elif statement=="strong":
            strong(no)
        elif statement=="composite":
            composite(no)
        elif statement == "harshad":
            harshad(no)
    else:
        speak("I can't understand your number please type your input ")
        no = int(input("Enter your number :: "))
        if statement=="amstrong":
            amstrong(no)
        elif statement=="happy":
            happyno(no)
        elif statement=="magic":
            magic(no)
        elif statement=="perfect":
            perfect(no)
        elif statement=="palindrome":
            palindrome(no)
        elif statement=="smith":
            smith(no)
        elif statement=="duck":
            duck(no)
        elif statement=="strong":
            strong(no)
        elif statement=="composite":
            composite(no)
        elif statement == "harshad":
            harshad(no)



def NCS_2(tag,query):
    if "amstrong" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"amstrong")
    elif "happy" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"happy")
    elif "magic" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"magic")
    elif "perfect" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"perfect")
    elif "palindrome" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"palindrome")
    elif "smith" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"smith")
    elif "duck" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"duck")
    elif "strong" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"strong")
    elif "composite" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"composite")
    elif "harshad" in tag:
        speak("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"harshad")






