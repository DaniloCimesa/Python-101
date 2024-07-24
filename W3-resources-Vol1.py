#W3 Resources
#https://www.w3resource.com/python-exercises/python-basic-exercises.php

#excercise1
string=  '''
Twinkle, twinkle, little star,
    How I wonder what you are! 
        Up above the world so high, 
        Like a diamond in the sky. 
Twinkle, twinkle, little star, 
    How I wonder what you are
'''
print(string)

string2= "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are"
print(string2)

#excercise2

import platform
print ('Python version is: '+str(platform.python_version()))

#excercise3

import datetime
current_datetime=datetime.datetime.now()
print('Current Datetime is: ' +str(current_datetime))

#excercise4

from math import pi

def func ():
    radius=input('Enter radius in meters please:')
    area=float(radius)**2*pi
    print('Circle area is: '+str(area)+' square meters')
    
func()

#excercise5

def func1():
    name=input('Your first name please:')
    surname=input('Your lastname please:')
    print('Hello 'surname+' '+name)
    
func1()

#excercise6

data_input=input("Input comma separated data:")
listed=data_input.split(',')
tupled=tuple(listed)
print('This is a tuple: ', tupled)
print('This is a list: ', listed)

#excercise7

def extension():
    filename=input('Write filename please:')
    chartofind='.'
    place=filename.find(chartofind)
    exten=filename[place+1:]
    print(exten)
    
extension()

filenm='danilo.cimesa.d'
extens=filenm.split('.')
print(extens[1])

#excercise8

color_list = ["Red","Green","White" ,"Black"]
print (color_list[0], color_list[-1])

#excercise9

from datetime import datetime 

exam_st_date='11,12,2024'
date2=datetime.strptime(exam_st_date, "%d%m%Y")
date3=datetime.strftime(date2,"%d/%m/%Y")

print('The examination will start from: ', date3)

#excercise10

def func2():
    while True:
        inppt=input('Input number:')
        try:
            number=int(inppt)
            number2=str(number)
            aa=number2*2
            aaa=number2*3
            print(number+int(aa)+int(aaa))
            return
        except ValueError:
            print('Thats not a valid integer.')
        
func2()

#excercise11

print(abs.__doc__)
#or
print(help(abs))

#excercise12

import calendar

def yearmonth():
    year=input('Input year:')
    month=input('Input month:')
    month_calendar = calendar.month(int(year), int(month))
    print(month_calendar)
    
yearmonth()

#excercise13

string='''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

print(string)

#excercise14

from datetime import date

def date_difff(date1,date2):
    date_diff=date2-date1
    #print('Difference between two dates is:'+str(date_diff))
    return date_diff.days

date1=date(2024,2,7)
date2=date(2024,7,7)

print('Difference is: '+str(date_difff(date1,date2))+' days')

#excercise15

from math import pi

def Volume():
    r=input('Input radius of a sphere: ')
    V=(4/3)*int(r)**3*pi
    print(V)
    
Volume()

#excercise 16

def NumCheck():
    a=input('Input number:')
    b=17
    c=int(a)
    if c<b:
        print(b-c)
    else:
        print(2*abs(c-b))

#excercise17

def function3(n):
    return abs(n-1000)<=100 or abs(n-2000)<=100

#excercise18

def functionsum():
    a=input('Input first number:')
    b=input('Input second number:')
    c=input('Input third number:')
    a1=int(a)
    b1=int(b)
    c1=int(c)
    if a1==b1==c1:
        return 3*(a1+b1+c1)
    else:
        return a1+b1+c1
    

functionsum()

#excercise19

def addIs (text):
    if text[:2]=='Is':
        return text
    else:
        return 'Is'+text
    
#excercise20

def returnco(string, n):
    return string*n

print(returnco('Branko',2))

#excercise21

def EvenOrOdd ():
    try:
        numb=int(input('Input number:'))
        if numb%2==0:
            print('Number is even!')
        else:
            print('Number is odd!')
    except ValueError:
        print('Num is not int')
        
#excercise22

def num_4_count(n):

    count=0

    for i in n:
        if i==4:
            count=count+1

    return count

#excercise23

def func_string(text,n):
    minlen=2
    if len(text)<minlen:
        return text*n
    else:
        return text[:2]*n
    
#excercise24

def Vowel():
    n=input('Input letter:')
    vowels=('a','e','i','o','u')
    if n in vowels:
        return True
    else:
        return False

#excercise25

def is_in(narray,a):
    if a in narray:
        return True
    else:
        return False
    

#excercise26

def print_histogram(counts):
    string='*'
    for count in counts:
        print(string * count)

#excercise27

def list_concatenation(lista):
    string1=''.join(map(str,lista))
    return string1

#excercise28

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
]

for i in numbers:
    if i%2==0:
        print(i)
    elif i==237:
        print(i)
        break

#excercise29

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1-color_list_2)

#excercise30

def triangle_area ():
    height=input('Input height of a triangle:')
    base=input('Input base of a triangle:')
    try:
        height1=int(height)
        base1=int(base)
        if isinstance(height1, int) and isinstance(base1, int):
            area=height1*base1*0.5
            return area
        else:
            return None
    except ValueError:
        print('Its not an integer!')
        return None

#excercise31
import math

a=60
b=48

gcd=math.gcd(a,b)
print(gcd)

#euclide Algorithm

def euclide_gcp(a,b):
    while b!=0:
        a,b=b , a%b
        return a
    
euclide_gcp(10,5)
