#page 317 program 4, NCERT
string=input("some string: ")
summ=0
for character in string:
    if character.isdigit():
        summ+=int(character)
print("sum of characters in given line is", summ)
