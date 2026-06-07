string = input("string: ")
character = input("character to count: ")
print("in", string, character, "'s found @", end=" ")
for char in range(len(string)):
    if string[char] == character:
        print(char, end=", ")
