import random as r 
import sys
class NumberGuessing(object): #class

    def __init__(self): #constructor 
        self.LOWER=1
        self.HIGHER=100

    def random_number(self):  #this function generates a random number using random module 
        return r.randint(self.LOWER,self.HIGHER)
    
    def start(self): 
        chances=0
        randomNumber = self.random_number() 

        print(f"Enter the number from {self.LOWER} to {self.HIGHER}:") #f strings 

        while True:
            user = int(input("Enter a number:"))
            if user == randomNumber:
                print(f"Hurray! you got it in {chances+1} step{'s' if chances> 1 else ''}")
                sys.exit(0)

            elif user > randomNumber:
                print("-> Your number is greater than the number ")
            else:
                print("-> Your number is less than the number")

            chances+=1



NumberGuessingGame=NumberGuessing() #creating a objects for NumberGuessing f

NumberGuessingGame.start()

        
