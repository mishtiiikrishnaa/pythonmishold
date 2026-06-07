#WAP to create a dictionary. display items of dictionary,
#keys of dictionary, values. use get method to display
#defined error msg. use pop(), popitem(),sorted.
d={1: "hi",2:"how",3:"what",4:"when",5:"why"}
print(d.keys())
print(d.items())
print(d.values())
k=int(input("enter a number? "))
print(d.get(k,"key does not exist"))
if k in d:
    print(d.pop(k))
print(d.popitem())
print(sorted(d))
print(sorted(d,reverse=True))
print(sorted(d.items()))
print(sorted(d.items(),reverse=True))