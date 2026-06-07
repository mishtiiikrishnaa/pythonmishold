# create a dictionary with book author, book name and year of publishing. obtain
# dictionary by changing year of publication as requested by user.
d,yop = {},{}
d["book name"] = input("book name? ")
d["book author"] = input("book author? ")
d["year of publishing"] = input("year of publishing? ")
print(d)
yop["year of publishing"] = input("year of publishing of above book? ")
d.update(yop)
print(d)
