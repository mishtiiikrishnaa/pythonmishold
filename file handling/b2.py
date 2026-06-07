import pickle
l=["lol"]
f=open("tezt.bin","wb")
pickle.dump(l,f)
print("added to binary file")
f.close()
f=open("tezt.bin","rb")
l1=pickle.load(f)
print("binary file: ")
print(l1)
f.close()


