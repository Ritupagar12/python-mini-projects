# Set Creation

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Methods
s1.add(6)
print(s1)
s1.update([7,8])
print(s1)
s1.remove(2)
print(s1)
s1.discard(10)  # no error if not present
print(s1)
s_copy = s2.copy()
print(s_copy)

# Operations
print("Union: ", s1.union(s2))
print("Intersection: ", s1.intersection(s2))
print("Difference: ", s1.difference(s2))
print("Symmetric Difference: ", s1.symmetric_difference(s2))

s1.clear()
print(s1)
