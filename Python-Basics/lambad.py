people = [
    {"name" : "harry", "house":"gryffindor"},
    {"name" : "cho", "house":"Ravenclaw"},
    {"name": "draco", "house":"Slytherin"}

]



# function
people.sort(key=lambda person: person["name"])

print(people)