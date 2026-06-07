# page 312, program 10
string = input("give a word: ")
mid = int(len(string) / 2)
backwards = -1
for character in range(mid):
    if string[character] == string[backwards]:
        character += 1
        backwards -= 1
    else:
        print(string, "ain't a palindrome")
        break
else:
    print(string, "'s a palindrome")
