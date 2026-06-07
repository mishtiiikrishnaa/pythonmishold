#create a dictionary to read a record with
#book author, title, price for as long as the user wants to.
d={}
while True:
    buth=input("book name, authored by: ")
    pric=int(input("price: "))
    d[buth]=pric
    cho=input("do you want to enter more? y/n: ")
    if cho=="y":
        c=True
    else:
        break
print(d)
