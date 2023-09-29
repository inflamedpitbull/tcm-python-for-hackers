valid = True
not_valid = False

print(valid)
print(not_valid)

print(valid == True)
print(not_valid == True)

print(valid != True)
print(not_valid != True)

print(not valid)
print(not not_valid)

print((10 < 9) == True)
print((10 == 10) == True)
print((10 >= 10) == True)
print((10 <= 10) == True)
print((10 > 9) == True)

print((10 < 9))
print((10 == 10))
print((10 >= 10))
print((10 <= 10))
print((10 > 9))

print("------")
print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)

print(bool(0))
print(bool(1))

print(bool(0) == False)
print(bool(1) == True)

print(10 + 10)
print(10 - 10)
print(10 / 10)
print(10 // 10) #floor divisinon
print(10 // 3)

#https://www.w3schools.com/python/python_operators.asp
print(10 * 10)
print(10 ** 10)
print(10 % 10)
print(10 % 3)

x = 10
print(x)
x = x + 1
print(x)

x += 1
print(x)

x -= 1
print(x)

x *= 5
print(x)

x /= 5 
print(x)

x = 13
print(bin(x))
print(bin(x)[2:].rjust(4,"0"))

y = 5
print(bin(y)[2:].rjust(4,"0"))

print(bin( x & y)[2:].rjust(4,"0"))

print(x & y)

print(bin( x | y)[2:].rjust(4,"0")) #https://www.prepbytes.com/blog/python/and-operator-in-python/#:~:text=In%20Python%2C%20the%20%22%26%22,the%20same%20position%20are%201.

print(bin( x >> 1)[2:].rjust(4,"0")) #bitshift