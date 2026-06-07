#function w/ argument but no return
def f1(arg):
    print("\tinside f1(arg):")
    print("\tvalue received in 'arg' as",arg)
    arg+=2
    print("\t\targ+=2")
    print("\tvalue of 'arg' now changes to",arg)
    print("\tgoing back to f1(arg)...")
#main
n=3
print("calling f1(arg) by passing 'n' with value",n)
f1(n)
print("back from f1(arg); value of n remains",n)
