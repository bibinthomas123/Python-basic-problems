# A program to convert radian to degree
# Formula => degree = radian x 180/ pie 

import math 

pi = math.pi  #Getting the pi value from the math module 

radian = int(input("Enter the radian value:")) #takes the input from the user 

degree = radian * 180/pi  #formula 
 
print("the degree of {0} radian is :{1:.2f}".format(radian,degree)) # the format is used to insert a value into the sting instead of concatination 
# where {0} indicate the first variable inside the .format and {1} for the second var in the .format 
#:.2f is used to truncate into 2 decimal places ex 3.14 instead of  3.1456896568523