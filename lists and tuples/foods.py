myfood=["pizza","falafel","carrot cake"]
friendfoods=myfood[:]
print("my fav foods are: ", myfood)
print("my friends fav foods are: ",friendfoods)
myfood.append("cannoli")
friendfoods.append("ice cream")
print("my fav foods are:")
for fav in myfood:
    print(fav)
print("my friends fav foods are: ")
for fave in friendfoods:
    print(fave)

