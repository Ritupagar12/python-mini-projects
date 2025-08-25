# Dictionary creation
person = {"name": "Ritu", "age": 25}

# Access keys, values, items
print(person.keys())    #dict_keys(['name', 'age'])
print(person.values())  #dict_values(['Ritu', 25])
print(person.items())   #dict_items([('name', 'Ritu'), ('age', 25)])
 
# Update Value
person["age"] = 26

# Add new key
person["city"] = "Auckland"
print("Updated Dictionary: ",person)

# Delete key
del person["city"]
print("Updated Dictionary: ",person)
