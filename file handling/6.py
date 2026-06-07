#code snippet 8
fileout=open("sampled.dat","w")
for i in range(5):
    name=input("name: ")
    fileout.write(name)
fileout.close()

#code snippet 9
fileout=open("sampled1.dat","w")
for i in range(5):
    name=input("name: ")
    fileout.write(name)
    fileout.write("\n")
fileout.close()

