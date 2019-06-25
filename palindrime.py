while(1):
    num=int(input("Enter the number to check palindrome or not :\n"))
    orig=num;
    ans=0
    while(num!=0):
        rem=num%10
        ans=ans*10+rem
        num=num//10
    if orig==ans:
        print("Given number is Palindrome :",orig)
    else:
        print("Given number is not palindrome :",orig)


