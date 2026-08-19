for i in range(1000,10000):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print("Smallest 4 digit no.",i)
        break
