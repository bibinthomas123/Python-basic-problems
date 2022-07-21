import sys 
import os 
import time
def again():
    print(''' To recalculate again please confirm
            Press Y (yes) or N (no)''')
    user = str(input()[0]) #takes only a single character 
    if user.upper() == "Y":
        operation()
    else:
        print("see you later")
        time.sleep(2)
        os.system("cls")#clears the console screen 

def operation():
    CRED = '\033[91m'  #Color codes
    CEND = '\033[0m'

    try:    #catchs the error 
    #input section 
        first = int(input("Enter the first number: "))
        second = int(input("Enter the second number: "))

    except ValueError:
        print(CRED + "Error, does not compute! Enter a digit" + CEND)
        sys.exit()   # Breaks the flow of the code if error is raised 


    sign = input('''Enter the sign
                + for addition 
                - for subtraction
                * for mutlipication 
                / for divison    
    ''')[0]


    if sign == "+":
        print (first + second )
    elif sign == "-":
        print (first - second )
    elif sign =="*":
        print (first * second)
    elif sign == "/":
        print (first / second)
    else:
        print(CRED + "Error,INVALID OPERATOR " + CEND)
    again()

operation()
