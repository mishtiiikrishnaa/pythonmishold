#3. Read a text & convert it into a list.WAP to count the number of letters in each
#item without using len()
string=input("enter some text: ")
lyst=string.split()
print("list of words in text: ",lyst)
letterc=0
lc=[]
for word in lyst:
    for letter in word:
        letterc+=1
    lc.append(letterc)
    letterc=0
print("letter count of each word:",lc)

    
    
        
        
