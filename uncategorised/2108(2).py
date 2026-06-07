#program 21, page 155, question bank
A=int(input("enter a number: "))
B=int(input("enter another number: "))
C=int(input("enter a third number: "))
if A>B>C:
    print (C, B, A)
if A>C>B:
    print (B, C, A)
if B>A>C:
    print (C, A, B)
if B>C>A:
    print (A, C, B)
if C>B>A:
    print(A, B, C)
if C>A>B:
    print(B, A, C)
elif A==B==C:
    print(A, B, C)
    
