for i in range(999,99,-1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        break
print("largest 3 digit no:",i)