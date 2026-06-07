pizzas=["dominos", "mom's", "pizza hut"]
for pizza in pizzas:
    print(f"i'm good with {pizza}")
print("i really don't like pizza as much as i love pasta,\nbut i'll take it over KFC's burgers any day.\npizzas are okay.\ni don't hate them.")
friendpizzas=pizzas[:]
pizzas.append("mushroom pizza")
friendpizzas.append("cheese pizza")
print("my fave pizzas are:")
for piz in pizzas:
    print(piz)
print("my friends fave pizzas are: ")
for piza in friendpizzas:
    print(piza)