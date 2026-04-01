string=input('Enter a string: ')
freq={}
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print("Letter Frequency: ")
for key,value in freq.items():
    print(key,":",value)