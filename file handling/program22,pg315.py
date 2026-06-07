address=input("house address: ")
city=input("city: ")
for character in city:
    if character.isdigit():
        print(character, end="")