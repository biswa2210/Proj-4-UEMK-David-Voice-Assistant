import pywhatkit
from say import speakNCS
import math
from Listen import  takeCommand
from CGA import controlGoogleAutomation
#1.EvenOdd
def EvenOddCheck(n):
    if n % 2 == 0:
        speakNCS("It is Even Number")
    else:
        speakNCS("It is Odd Number")
    speakNCS("A number is even if it is perfectly divisible by 2. When the number is divided by 2, we use the remainder operator % to compute the remainder. If the remainder is not zero, the number is odd")
    speakNCS("do you want to know more about Even and Odd numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans,"Even Odd Number")
#2.Prime
def PrimeCheck(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):

            if (num % i) == 0:
                speakNCS("It is not a prime number")
                break
        else:
            speakNCS("It is a prime number")

    else:
        speakNCS("It is not a prime number")
    speakNCS("Prime numbers are the numbers that have only two factors, that are, 1 and the number itself. ")
    speakNCS("do you want to know more about Prime numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans,"Prime Number")
#4.Pronic
def pronic(n):

    i = 0
    flag = 0

    while i <= (int) (math.sqrt(n)):
        if n == i * (i + 1):
           flag = 1
           break
        i = i + 1

    if flag == 1:
        speakNCS("It is a Pronic Number." )
    else:
        speakNCS("It is Not a Pronic Number." )
    speakNCS("A pronic number is a number which is the product of two consecutive integers.")
    speakNCS("do you want to know more about Pronic numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Pronic Number")

#6.Automorphic
def isAutomorphic(N):
    flag=0
    sq = N * N
    if (N % 10 != sq % 10):
        flag=0
        N //= 10
        sq //= 10
        flag=1

    if (flag==1):
        speakNCS("It is Not Automorphic.")
    else:
        speakNCS("It is Automorphic")
    speakNCS("An automorphic number is an integer whose square ends with the given integer.")
    speakNCS("do you want to know more about Automorphic numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Automorphic Number")
#7.Neon
def isNeon(n):
    Sum = 0

    squr = math.pow(n, 2)

    while squr > 0:
        rem = squr % 10
        Sum = Sum + rem
        squr = squr // 10


    if Sum == n:
        speakNCS("It is Neon Number.")
    else:
        speakNCS("It is not Neon Number.")
    speakNCS("A neon number is a number where the sum of digits of square of the number is equal to the number.")
    speakNCS("do you want to know more about Neon numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Neon Number")
#8.Buzz
def isBuzz(num):
    if num % 7 == 0 or num % 10 == 7:
        speakNCS("It is Buzz Number.")
    else:
        speakNCS("It is not Buzz Number.")
    speakNCS("Buzz number is another special number in Java that ends with digit 7 or divisible by 7.")
    speakNCS("do you want to know more about Buzz numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Buzz Number")
#9.Negative
def isNegative(n):
    if(n<0):
        speakNCS("It is Negative Number.")
    else:
        speakNCS("It is not Negative Number.")
    speakNCS("A negative number is a number whose value is always less than zero and it has a minus sign before it.")
    speakNCS("do you want to know more about Negative numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Negative Number")
#11.Amicable
def isAmicable(x):
    y=int(input())
    sum_x=0
    sum_y=0
    for each in range(1,x):
        if(x%each==0):
           sum_x=sum_x+each
    for i in range(1,y):
        if(y%i==0):
           sum_y=sum_y+i
    if(sum_x==y and sum_y==x):
        speakNCS("They are Amicable numbers")
    else:
        speakNCS("No they are not Amicable")
    speakNCS("Amicable numbers are two different natural numbers related in such a way that the sum of the proper divisors of each is equal to the other number.")
    speakNCS("do you want to know more about Amicable numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Amicable Number")
#12.Strong
def isStrong(num):
    sum = 0
    temp = num
    while (num):
        i = 1
        fact = 1
        rem = num % 10
        while (i <= rem):
            fact = fact * i
            i = i + 1
        sum = sum + fact
        num = num // 10
    if (sum == temp):
        speakNCS("It is Strong Number.")
    else:
        speakNCS("It is not Strong Number.")
    speakNCS("Strong number is a special number whose sum of the factorial of digits is equal to the original number. ")
    speakNCS("do you want to know more about Strong numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Strong Number")

#14.Spy
def checkSpy(num):
    sums = 0
    product = 1
    while num > 0:
        digit = num % 10
        sums = sums + digit
        product = product * digit
        num = num // 10

    if sums == product:
        speakNCS("It is Spy Number.")
    else:
        speakNCS("It is not Spy Number.")
    speakNCS("A number is said to be a Spy number if the sum of all the digits is equal to the product of all digits. ")
    speakNCS("do you want to know more about Spy numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Spy Number")
#15.Ugly
def isUgly(num):
    flag =0
    if num == 0:
        flag =0
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    flag = 1
    if (flag == 1):
        speakNCS("It is Ugly Number.")
    else:
        speakNCS("It is not Ugly Number.")
    speakNCS("Ugly numbers are numbers whose only prime factors are 2, 3 or 5. ")
    speakNCS("do you want to know more about Ugly numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Ugly Number")
#16.Positive
def isPositive(n):
    if (n>0):
        speakNCS("It is Positive Number.")
    else:
        speakNCS("It is not Positive Number.")
    speakNCS("Positive numbers are numbers who are always greater than 0. ")
    speakNCS("do you want to know more about Positive numbers ?")
    speakNCS("please say yes or no")
    ans = takeCommand()
    controlGoogleAutomation(ans, "Positive Number")

def notRecogCheck(var,statement):
    if var is not "None":
        no = int(var)
        print("Input :: " + str(no))
        if statement == "evenOddCheck":
            EvenOddCheck(no)
        elif statement == "primecheck":
            PrimeCheck(no)
        elif statement == "proniccheck":
            pronic(no)
        elif statement == "automorphiccheck":
            isAutomorphic(no)
        elif statement == "neoncheck":
            isNeon(no)
        elif statement == "buzzcheck":
            isBuzz(no)
        elif statement == "negativecheck":
            isNegative(no)
        elif statement == "amicablecheck":
            isAmicable(no)
        elif statement == "strongcheck":
            isStrong(no)
        elif statement == "spycheck":
            checkSpy(no)
        elif statement == "uglycheck":
            isUgly(no)
        elif statement == "positivecheck":
            isPositive(no)


    else:
        speakNCS("I can't understand your number please type your input ")
        no = int(input("Enter your number :: "))
        if statement=="evenOddCheck":
            EvenOddCheck(no)
        elif statement == "primecheck":
            PrimeCheck(no)
        elif statement == "automorphiccheck":
            isAutomorphic(no)
        elif statement == "neoncheck":
            isNeon(no)
        elif statement == "buzzcheck":
            isBuzz(no)
        elif statement == "negativecheck":
            isNegative(no)
        elif statement == "amicablecheck":
            isAmicable(no)
        elif statement == "strongcheck":
            isStrong(no)
        elif statement == "spycheck":
            checkSpy(no)
        elif statement == "uglycheck":
            isUgly(no)
        elif statement == "positivecheck":
            isPositive(no)


def NCS_1(tag,query):
    if "evenOddCheck" in tag:
        speakNCS("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"evenOddCheck")
    elif "primecheck" in tag:
        speakNCS("Tell me the number")
        number=takeCommand()
        notRecogCheck(number,"primecheck")
    elif "proniccheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "proniccheck")
    elif "automorphiccheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "automorphiccheck")
    elif "neoncheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "neoncheck")
    elif "buzzcheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "buzzcheck")
    elif "negativecheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "negativecheck")
    elif "amicablecheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "amicablecheck")
    elif "strongcheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "strongcheck")
    elif "spycheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "spycheck")
    elif "uglycheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "uglycheck")
    elif "positivecheck" in tag:
        speakNCS("Tell me the number")
        number = takeCommand()
        notRecogCheck(number, "positivecheck")






