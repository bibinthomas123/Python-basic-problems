# taking the decimal value and converting it into the binary value 

def decimal(val):
    if val >1:
        decimal(val//2)  # using recursion floor division 
    print(val%2,end="")

if __name__ == "__main__":
    value = int(input("Enter the value :"))
    decimal(value)