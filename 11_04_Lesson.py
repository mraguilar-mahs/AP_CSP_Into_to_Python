#Lesson 1.6 Python - Class 11/04
#Std:
#Obj:

height = 4.6
weight = 110

#Condition: h >= 5 and w >= 110 <- Can ride
#Logical Opps: AND, OR, NOT opperations

if height >= 5:
    if weight >= 110:
        print("Ride!")
    else:
        print("No Ride!")
else:
    print("No Ride!") #How about weight? -> We don't know!
    # I know for a fact height is not met
    # Weight does not matter b/c height is not met.


#Conditions - effiecient: meaning they check for one or more conditions
#Logical Opps: AND, OR, NOT ->