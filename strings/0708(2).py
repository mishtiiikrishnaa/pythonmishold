#string pgm 9.1-reverse character printing
string1=(input("some word you'd like to slice: "))
print("The word, ", string1, "in the reverse order is: ")
for a in range (-1,(-len(string1)-1),-1):
    print(string1[a])
    
