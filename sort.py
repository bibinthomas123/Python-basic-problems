#Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be
#  one of the following values: asc, desc, and none.



print("Enter the range of the  list :",end="")
n = int(input()) #takes the count of number 

lists=[] #initalizing the array

order = input('''Enter the order of the list : 
                asc = increasing 
                desc = decreasing ''') #takes the order how should the data to be printed 

print("Enter the list values: ") #taking the numbers into the list 
for i in range(n):
    l = int(input())
    lists.append(l) #adding it to the list 
    

def sorts(lists,order): 
    if order =="asc":
        lists.sort() # if order = asc then the lists will be sorted in increasing order 
        return lists
    elif order == "desc":
        lists.sort(reverse=True) #if the order = desc then the lists will be sorted in descending order (reverse = True)
        return lists
    else: #if no value is given then the list will be returned unaltered 
        return lists


print(sorts(lists,order))


