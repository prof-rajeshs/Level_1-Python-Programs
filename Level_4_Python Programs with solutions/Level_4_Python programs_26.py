for i in range(100,1000):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
            break
print("Smallest 3 digit no:",i)