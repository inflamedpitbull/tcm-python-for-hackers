name = "hacker"
print(name)

name_length = 4
print(name_length)

name, name_length = "hacker", 4
print(type(name))
print(type(name_length))

name_length = int("4")
print(type(name_length))

name_list = ["123", "4565"]
print(type(name_list))

name1, name2 = name_list
print(name1)
print(name2)

name_tuple = ("1234", "4567")
print(type(name_tuple))

name_dictionary = {"hacker": 4, "malware":1}
print(type(name_dictionary))

name_boolean = True
print(type(name_boolean))

name_range = range(6)
print(type(name_range))

name_bytes = b"hacker"
print(type(name_bytes))

print(name_tuple)
print(name_list)
print(name_dictionary)
print(name_bytes)
print(name_boolean)
print(name_range)
