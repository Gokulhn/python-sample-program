def sumOfNum(num):
    sum=0
    while num!=0:
        n = num % 10
        sum += n
        num=num//10
    return sum

while True:
    number = int(input("Enter the number to find sum of digit :\n"))
    sum = sumOfNum(number)
    print(f"Sum of the entered digit is : {sum} ")


