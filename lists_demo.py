list1 = ["a", "b", "c", "d", "e", "f"]
print(list1)

list2 = ["a", 1, 2.0, ["a"], [], list(), ("a"), False]
print(list2)
print(type(list2))

print(list1[0])
print(list1[-1])

print(list2[3][0])
print(list2[3][-1])

list1[0] = "x"
print(list1)

del list1[0]
print(list1)

list1.insert(0, "a") #insert when you caraes about index
print(list1)

del list1[0]
print(list1)

list1 = ["a"] + list1
print(list1)

list1.append("g")
print(list1)

print(max(list1))
print(min(list1))

print(list1.index("c")) #find index

print(list1[list1.index("c")])

list1.reverse()
print(list1)

list1 = list1[::-1]
print(list1)

print(list1.count("a"))
list1.append("a")
print(list1.count("a"))

list1.pop()
print(list1)

list3 = ["h", "i", "j"]
print(list3)

list1.extend(list3)
print(list1)

list1.clear()
print(list1)

list4 = [8, 12, 5, 6, 17, 2]
print(list4)
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

list5 = list4
print(list4)
print(list5)

list5[2] = "x"
print(list4)
print(list5)

list6 = list4.copy() #make copy of the list so it's values won't be changed if you want to work on the list
print(list4)
print(list6)

list6[2] = "A"
print(list6)
print(list4)

list7 = ["1", "2", "3"]
print(list7)

list8 = list(map(float, list7)) #perform operatons on each element in a list
print(list8)