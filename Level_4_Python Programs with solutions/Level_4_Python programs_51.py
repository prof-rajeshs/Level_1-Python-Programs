#Get a string and a character from the user and find all the positions where the character present and print it
string = input("Enter a string: ")  
char = input("Enter a character: ")     
positions = []
for i in range(len(string)):
    if string[i] == char:
        positions.append(i)
print("The positions where the character is present are:", positions)