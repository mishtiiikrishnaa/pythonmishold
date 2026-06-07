print ("the loop with 'break' produces output as: ")
for m in range(1,11):
    if m%3==0:
        break
    else:
        print(m)
print ("the loop with 'continue' produces output as: ")
for m in range(1,11):
    if m%3==0:
        continue
    else:
        print(m)
