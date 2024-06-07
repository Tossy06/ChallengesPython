def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result
while True:      
    try:
        n = int(input("Enter a number: "))
        while n != 1:
            n = collatz(n)
        break  # Exit the loop when the sequence reaches 1
    except ValueError:
        print("Enter a correct value: ") 
        