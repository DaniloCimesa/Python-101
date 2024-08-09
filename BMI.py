
def input_f ():
    name=input("Enter your name:")
    height=int(input("Enter your height:"))
    weight=int(input("Enter your weight:"))
    print("My name is " +name+", I am "+str(height)+" centimeters tall"+" and I weigh "+str(weight)+" kilograms.")
    BMI=weight/((height*0.01)**2)
    Recommended_BMI=25*((height*0.01)**2)
    print("Your BMI is: "+str(BMI))
    print("Your recommended weight should be:"+str(Recommended_BMI))


input_f()

