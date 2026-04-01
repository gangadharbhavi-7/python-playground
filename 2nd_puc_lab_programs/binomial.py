def fact(n):
    if n<0:
        return "Factorial does not exist for negative numbers"
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input("Enter a n value: "))
factorial=fact(n)
print("The factorial of ",n," is ",factorial)
k=int(input("Enter the value of k: "))
binomial=fact(n)//(fact(k)*fact(n-k))
print("The binomial coefficient c(",n,"/",k,") is: ",binomial)