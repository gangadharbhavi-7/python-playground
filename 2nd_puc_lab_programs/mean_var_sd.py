n=int(input("Enter the number of elements: "))
l=[]
sum=0
for i in range(n):
    num=int(input("Enter a number: "))
    l.append(num)
    sum+=num
mean=sum/n
var=0
for i in l:
    var+=(i-mean)**2/n
sd=var**0.5
print("Mean: ",mean)
print("Variance: ",var)
print("Standard Deviation: ",sd)
