str1=input("some word: ")
str2=input("some another word: ")
print("OG strings: "+ str1 + ", " + str2) 
if str1 in str2:
    str3=(str2[:4] + "Restore")
print("final strings: " + str1 + ", " + str3)
