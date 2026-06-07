# page 305, program 9.11
set = input("enter a set of words: ")
subset = input("enter a set of words subset to above: ")
start, count = 0, 0
end = len(set)
while True:
    pos = set.find(subset, start, end)
    if pos != -1:
        count += 1
        start = pos + len(subset)
    else:
        break
    if start < len(set):
        continue
    break
print("no of occurrences of", subset, "is", count)
