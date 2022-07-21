#To check wheather the character entered is Vowel or not 

Char = input("Enter a character: ")[0] #takes only a single character as a input

vowel =["a","e","i","o","u"] # an array storing the vowels 

if Char in vowel:  #checks wheather the char var exists in the vowel array if its exists executes the following if statements 
    print("The char {0} is vowel".format(Char))
else: #else the executes the following statements 
    print("The Char {0} is not a vowel".format(Char))