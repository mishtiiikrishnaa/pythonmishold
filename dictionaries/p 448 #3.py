#p 448 type c #3
n={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
num=int(input("enter number: "))
for no in str(num):
    print(n.get(int(no)),end= " ")
    

