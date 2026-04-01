f0=0
f1=1
n=int(input("Enter the number of terms: "))
print("Fibonacci sequence: \n")
for i in range(n):
    if i==0:
        print(f0)
    elif i==1:
        print(f1)
    else:
        f2=f0+f1
        print(f2)
print("fibonacci sequence:")