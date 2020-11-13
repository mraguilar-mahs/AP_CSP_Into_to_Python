#Lesson 1.5 Python - Class 10/30
#Std:
#Obj:

#Casting -> Transform between diff data types

#name = input("Please enter your name: ")
#age = (int) (input("What is your age:")) #<- Age is being saved String

#age += 10 #<- Add 10, I am adding number 10. We can now do this b/c of cast.

#Example of String Concatination
#print("Hi " + name + " and welcome! Your age is: " + (str)(age))

#Logic/Conditionals
#Boolean -> True & False
#Condition: Is a choice or a set of choices:

#If___then____else structure
grade = 65
#Comparisons: <,>, <=, >=, ==, !=
if grade >= 70:
    print("Pass!")


#if ____ else

if grade >= 90:
    print("A")
else:
    print("Not an A")

#if____else if(0 to many) ____else:

if grade >= 90:
    print("A")
elif grade >= 80: # else if -> check again for the condition
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")

height = 4.6
weight = 110

#Condition: h >= 5 and w >= 110
#Logical Opps: AND, OR, NOT opperations

if height >= 5:
    if weight >= 110:
        print("Ride!")
    else:
        print("No Ride!")
else:
    print("No Ride!")

