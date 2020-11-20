import random
#Lesson 1.8 Python - Class 11/18
#Std:
#Obj:

#Agenda:
#AP CS A -> Java CS Course
#Lesson
#TBD:
#Quiz
#Assignment



#While Loop: Conditional: What allows you to stop the loop.
x = 1
while x < 10: #Good Rule: we change the var.
    print(x) # Body of the While
    x = x + 1 #Increment or Var Changer


#Random Numbers:
print(random.randint(1,10))
rand = random.randint(1,4)

#Chanlenge: Create a random number guesser.
#Code will: 1. Choose a random number. 2. Ask the user to input in the given range
# 3. Tell the user if they are right or not. 4. End Game if guessed correctly or continue
# going and ask again.

print("Welcome to number guesser. I am choosing a number 1 to 10")
randNnm = random.randint(1,10)
guess = input("Please enter a number 1 to 10:")



