#WAP to read a list of strings and cap the 1st letter
#of every word in the string and convert it to a tuple b4 printing
los=eval(input("enter list of strings: "))
lost=[]
for string in los:
    ns=string[0].upper()+string[1:-1]+string[-1]
    lost.append(ns)
print(tuple(lost))
