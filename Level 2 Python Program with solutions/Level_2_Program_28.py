n1=int(input("Enter the 1st no."))
n2=int(input("Enter the 2nd no."))
n3=int(input("Enter the 3rd no."))
max_n=max(n1,n2,n3)
while True:
    if max_n % n1==0 and max_n % n2==0 and max_n%n3==0:
        print("LCM=",max_n)
        break
    max_n=max_n+1