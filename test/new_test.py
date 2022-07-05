list_a = ["a", "b", "c"]
list_b = ["a", "b"]

list_c = list(set(list_a) - set(list_b))
print(list_c)