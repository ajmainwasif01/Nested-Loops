w = input("Enter your own word:")

c = input("Enter the letter:")

i = 0
count = 0
while (i < len(w)):
    if(w[i] == c):
        count = count + 1
    i += 1 

print("The total number of times has occured:" , count)   