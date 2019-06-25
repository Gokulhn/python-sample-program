import math
while True:
    num = int(input("Enter the number to check number is prime is not :\n"))
    if num >= 2:
        for i in range(2, num//2):
            if (num % 2) == 0:
                print(f"Given number is not a prime number :{num}")
                break
            else:
                print(f"Given Number is prime :{num}")
                break
    else :
        print("Number is not prime!!!")


