num  = input("Enter a number: ")

num = int(num)

if num <= 0:
    print("Number must be a positive integer")
else:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")