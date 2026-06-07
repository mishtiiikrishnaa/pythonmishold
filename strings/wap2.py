#create a dictionary to read a list of numerical elements. for each number in the list, write frequency of element as its value.
l=eval(input("numerical list: "))
d={}
for n in l:
    d[n]=l.count(n)
print(d)
