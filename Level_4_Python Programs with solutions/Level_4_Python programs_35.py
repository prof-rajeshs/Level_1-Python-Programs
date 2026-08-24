#Get 2 numbers from user and find the LCM of them
n1=int(input("Enter the number 1:"))
n2=int(input("Enter the number 2:"))
max_n=max(n1,n2)
while True:
    if max_n%n1==0 and max_n%n2==0:
        Lcm=max_n
        break
    max_n+=1
print("The LCM is:",Lcm)