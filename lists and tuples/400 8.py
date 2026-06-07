#page 400[8]
text=input("enter some text: ")
t1=text.split()
if len(t1)<1:
          print("bye")
else:
          t=[]
          for word in t1:
                    t.append(len(word))
          print(t1)
          tu=tuple(t)
          print("shortest word length: ",min(tu))
