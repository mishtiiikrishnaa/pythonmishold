rint=(input("what do u wanna convert? seconds, minutes or days? "))
if rint=="seconds":
    sec=int(input("enter time in seconds: "))
    print(sec, "seconds")
elif rint=="minutes":
    min=int(input("enter time in minutes: "))
    print(min*60,"seconds")
elif rint=="days":
    day=int(input("enter time in days: "))
    print(day*24*60*60, "seconds")
else:
    print("NO")