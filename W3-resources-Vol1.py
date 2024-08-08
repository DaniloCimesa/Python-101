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

#excercise32

import math

a=15
b=20

gcd=math.gcd(a,b)
lcm=abs(a*b)/gcd
print(lcm)

#excercise33

def sum_three (a,b,c):
    if a==b or a==c or b==c:
        return 0
    else:
        return a+b+c
    

#excercise34

def sum_two(a,b):
    if 15<=(a+b)<=20:
        return 20
    else:
        return a+b
    
#excercise35

def sum_ifs(a,b):
    if a==b or a+b==5 or abs(a-b)==5:
        return True
    else:
        return False
    
    
#excercise36
def sum_two_intgs(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    else:
        return "Its not intg"
    
#excercise37

def Details ():
    name='Danilo Cimesa'
    age=27
    residence='Mite Rankova 14, Pancevo, Srbija'
    print('Name: {} \nAge: {} \nResidence: {}'.format(name, age, residence))

#excercise38

a,b=(4,3)
result=a*a+2*(a*b)+b*b
print('({} + {})^2 = {}'.format(a,b,result))

#excercise39

amount=10000
interest=3.5
period=7

FutureValue=amount*(1+interest*0.01)**period
print(FutureValue)

#excercise40

def distance (x1,y1,x2,y2):
    d=(((x2-x1)**2+(y2-y1)**2))**(1/2)
    return d

#excercise41

import os
file_path=r'C:\Users\Danilo\OneDrive\Desktop\notepads\danilo.cimesa.txt'

if os.path.exists(file_path):
    True
else:
    False

#excercise42

import platform

bit_mode = platform.architecture()[0]
print(f"The Python shell is executing in {bit_mode} mode.")

#excercise43

import platform

os_name = platform.system()
platform_name = platform.platform()
release_info = platform.release()

print(f"OS Name: {os_name}")
print(f"Platform: {platform_name}")
print(f"Release: {release_info}")

#excercise44

import site

site_packages = site.getsitepackages()
print(site_packages)

#excercise45
#/

#excercise46

import inspect
import os

current_file_path = os.path.abspath(inspect.getfile(inspect.currentframe()))

print("Current file path:", current_file_path)
print("Current file name:", os.path.basename(current_file_path))

#excercise47

import multiprocessing

# Get the number of CPUs available
num_cpus = multiprocessing.cpu_count()

print(f"Number of CPUs available: {num_cpus}")

#excercise48

num='234.567'
print(num)
num2=float(num)
print(num2)
print((int(num2)))

#excercise49

def list_files():
    import os
    directory=input('Input dir:')
    files=os.listdir(directory)
    print(files)
    
#excercise50

for i in range(1,10):
    print('*', end='')
print("\n")

#excercise51
#/

#excercise52
import sys

def print_to_stderr(message):
    print(message, file=sys.stderr)

# Example usage
print_to_stderr("This is an error message.")

#excercise53
import os

print(os.environ)

#excercise54

import os

user=os.getlogin()

print(user)

#excercise55

import socket

hostname = socket.gethostname()
ip_addresses = socket.getaddrinfo(hostname, None)

ip_add=[ip[-1][0] for ip in ip_addresses]
print(ip_add)

#excercise56

import os
import shutil

def get_console_size():
    size = shutil.get_terminal_size((80, 20))  # Default values if size can't be determined
    width = size.columns
    height = size.lines
    return width, height

if __name__ == '__main__':
    width, height = get_console_size()
    print(f"Width: {width}")
    print(f"Height: {height}")


#excercise57
import time

def sample_method():
    # Example method to measure execution time
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

begin_time=time.time()
result=sample_method()
end_time=time.time()
exec=end_time-begin_time

print(exec)

#excercise58

def sum_intg(y):
    total=0
    for i in range(1,y+1):
        total+=i
    return total

#or
def sum_intg2(y):
    return (y*(y+1))//2

#excercise59

def height_convert():
    height=input("Input height(feet, inches): ").split(',')
    heightincm=str(float(height[0])*30.48 +float(height[1])*2.54)
    print("Your height in cm is: "+heightincm)

#excercise60
import math

a=float(input("1st side"))
b=float(input("2nd side"))

c=math.sqrt(a**2+b**2)
print(c)

#excercise62

def time_convert():
    days=int(input("Input number of days:"))
    hours=int(input("Input number of hours:"))
    minutes=int(input("Input number of minutes:"))
    seconds=int(input("Input number of seconds:"))
    
    time_in_sec=days*24*60*60 + hours*60*60 + minutes*60 + seconds
    
    print("For: "+str(days)+" days, " + str(hours)+" hours, " + str(minutes)+" minutes and" +str(seconds)+" seconds")
    print("Time in seconds is: "+str(time_in_sec))
