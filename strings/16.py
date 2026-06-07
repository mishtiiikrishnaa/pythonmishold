inp1=input("enter 3 words: ")
inp=list(inp1.split(", "))
if len(inp[2])>len(inp[1])>len(inp[0]):
    print(len(inp[2]))
elif len(inp[1])>len(inp[0])>len(inp[2]):
    print(len(inp[1]))
elif len(inp[0]) > len(inp[2]) > len(inp[1]):
    print(len(inp[0]))

