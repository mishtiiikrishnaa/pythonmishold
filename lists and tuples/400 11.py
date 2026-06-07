seq_a=eval(input("enter a tuple: "))
seq_b=eval(input("enter another tuple: "))
sea,seb=list(seq_a),list(seq_b)
for el in sea:
    if el in seb:
        print("true")
    else:
        print("false")
        break