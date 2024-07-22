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

