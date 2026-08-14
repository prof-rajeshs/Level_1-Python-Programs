n1=int(input("Enter the 1st no."))
n2=int(input("Enter the 2nd no."))
hcf=1
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print("HCF=",hcf)