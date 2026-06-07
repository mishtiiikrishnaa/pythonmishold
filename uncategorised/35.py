stri=str(input("number: "))
sum=0
for ch in stri:
    if ch.isdigit():
        sum+=int(ch)
print(sum)