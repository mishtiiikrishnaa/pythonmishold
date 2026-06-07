#pg 375 11.6
T=("hello","isn't","python","fun","?")
for i in T:
    print(i)
    print(T.index(i),end=" ")
    print(-(len(T)-T.index(i)))
