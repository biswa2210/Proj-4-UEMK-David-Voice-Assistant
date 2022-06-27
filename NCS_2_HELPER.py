import pywhatkit
from say import speak,speakNCS
from Listen import  takeCommand


#----- POWER OF A NO.-----#
def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)

    return x * power(x, y // 2) * power(x, y // 2)

#----- ORDER OF A NO. // DIGIT COUNT OF A NO. -----#
def order(x):
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10

    return n

#----- SUM OF (DIGIT)^2 OF A NO.-----#
def digitsquaresum(no):
    rem = sum = 0
    while (no != 0):
        rem = no % 10
        sum = sum + power(rem, 2)
        no = no // 10
    return sum

#----- SUM OF DIGITS OF A NO.-----#
def digitsum(no):
    rem = sum = 0
    while (no != 0):
        rem = no % 10
        sum = sum + rem
        no = no // 10
    return sum

#----- REVERSE A NO. -----#
def reversenum(no):
    rem = rev = 0
    while (no != 0):
        rem = no % 10
        rev = rev*10 + rem
        no = no // 10
    return rev


#----- PRIME NO. -----#
def isprimeno(no):
    c=0
    i=2
    while (i<no):
        if(no%i==0):
            c=c+1
        i=i+1
    if(c==0):
        return True
    else:
        return False

