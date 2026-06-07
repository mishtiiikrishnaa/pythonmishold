string=input("a bunch of characters: ")
up, low ,digit=0, 0, 0
for ch in string:
    if ch.isupper():
        up+=1
    elif ch.islower():
        low+=1
    elif ch.isdigit():
        digit+=1
print("the no. of uppercases, lowercases & "
      "digits in", string, "are",
      up, ",",
      low, "&", digit, "respectively.")


