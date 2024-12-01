def is_palindrome(n,temp,rev=0):
    if n==0:
        if temp==rev:
            return "The number is palindrome"
        else:
            return "The number is not a palindrome"
    else:
        dig=n%10
        rev=rev*10+dig
        n=n//10
        return (n,temp,rev)   
n=int(input("Enter the number"))   
result =is_palindrome(n,n)
print(result)