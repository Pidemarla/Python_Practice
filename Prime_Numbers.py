number = int(input("Enter a Number: "))

count = 0
if number == 0 or number == 1 or number == 2:
    print("Entered Number is a Prime Number")
elif number< 0:
    print("Number Cannot be Negative")
else:
    for i in range(2,number-1):
        if number % i == 0:
            count = count +1
            if count == 1:
                break

    if count == 0:
        print("Entered Number is Prime Number") 
    else:
        print("Entered Number is not a Prime Number")