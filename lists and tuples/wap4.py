#CAD, use copy and set default.
cad={1: "hi",2:"how",3:"what",4:"when",5:"why"}
cad1=cad.copy()
cad.setdefault(6,"where")
cad.setdefault(5,"Why")
print(cad.setdefault(4,"Why"))
print (cad)
print (cad1)
