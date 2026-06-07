principle=int(input("give a principle amount: "))
time=int(input("give the no. of years : "))
rate=int(input("give the rate of interest: "))
interest=(principle*time*rate)/100
print(f"the simple interest for a principle amount of "
      f"Rs {principle} for {time} years "
      f"with a rate of interest {rate}% is "
      f"{interest} rupees.")