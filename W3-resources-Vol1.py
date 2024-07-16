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
