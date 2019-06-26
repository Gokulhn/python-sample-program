def reverse(num):
    ans = 0
    while (num != 0):
        rem = num % 10
        ans = ans * 10 + rem
        num = num // 10
    return ans

def updateByOne(num):
    ans = 0
    while(num != 0):
        rem = num % 10;
        if rem < 9:
            ans = ans * 10 + (rem+1)
            num = num // 10
        else:
            ans = ans * 10
            num = num // 10
    return ans

while True:
    digit = int(input("Enter the number to get updated by one :\n"))
    num = reverse(digit)
    print(f"Updated value is :{updateByOne(num)}")
