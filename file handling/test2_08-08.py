import pickle
l1=['hi','test','my friends are the worst lol']
f=open("test.dat",'wb')
pickle.dump(l1,f)
print('added to binary file')
f.close()
f=open('test.dat','rb')
l=pickle.load(f)
print("bin file:")
print(l)
f.close()
