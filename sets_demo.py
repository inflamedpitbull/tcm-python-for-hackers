set1 = {"a", "b", "c"}
print(set1)
print(type(set1)) #sets are not ordered

set2 = {"a", "a", "a"} #can't contain duplicates
print(set2)
print(len(set2))

set3 = {"a", 0, True}
print(set3)

set4 = set(("b", 1, False))
print(set4)

set1.add("d")
print(set1)

set3.update(set4)
print(set3) #can't contain duplicates so 1 or True, 0 or False will be omitted

list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

set5 = {4, 5, 6}
set6 = set4.union(set5)
print(set6)

set4.remove(4) #can only remove the value that exists
print(set4)

set4.discard(4)
print(set4) #discard won't throw error if the element doesn't exist

print(set1)
set1.pop()
print(set1) #only use pop when not care about the order of the set