def divisiion(divide):
    try:
        return n / divide
    except ZeroDivisionError:
        print("Incorrect value, please try again: ")
        
n = int(input("Enter a number to divide: "))
divide= int(input("Enter the number that divides: "))
print(divisiion(divide))