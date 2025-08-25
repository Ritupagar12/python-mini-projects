l = [1, 2, 3]
t = (4, 5, 6)

print("Original List: ", l)
l.append(7)
l.insert(1, 10)
print("Modified List: ", l)

print("Original Tuple: ", t)
list_from_tuple = list(t)
list_from_tuple.append(8)
print("Tuple converted to List: ", list_from_tuple)
tuple_from_list = tuple(l)
print("List converted to Tuple: ", tuple_from_list)
