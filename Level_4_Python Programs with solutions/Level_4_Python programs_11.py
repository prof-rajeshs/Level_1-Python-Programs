n=int(input("Enter a 4digit no.:"))   #7638
n1=(n//1000)   #7
n2=(n//100)%10  #6
n3=(n%100)//10    #3
n4=(n%10)      #8
sum=n1+n2+n3+n4
print("The sum of the digits is:", sum)     #24