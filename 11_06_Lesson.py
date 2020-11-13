import random
#Lesson 1.7 Python - Class 11/06
#Std:
#Obj:

height = 5.1
weight = 110

#Condition: h >= 5 and w >= 110 <- Can ride
#Logical Opps: AND, OR, NOT opperations

#if height >= 5:
    #if weight >= 110:
    #    print("Ride!")
    #else:
    #    print("No Ride!")
#else:
    #print("No Ride!") #How about weight? -> We don't know!
    # I know for a fact height is not met
    # Weight does not matter b/c height is not met.


#Conditions - effiecient: meaning they check for one or more conditions
#Logical Opps: AND, OR, NOT ->

if height >= 5 and weight >= 110:
    print("Ride!")
else:
    print("No Ride!")


#For and While Loops
# What is a loop -> Repeating: a piece of code of a certain set of actions.
# For loop allows us to repeat code a certain amount (finite) of time, finite "iteration"

# 1,2,3,4,5,6,7,8,9,10
# range(inclusive, exclusive)
for x in range(1,11): # x <- var that changes, we use.
    print(x)

#while loop - repeat code, where we don't know the cetain of iterations
#Create a random number guesser -


#Have left: 
# While Loops
# Functions/Methods
#Classes/Objects
#List/Arrays
# And a lot more....



