f = open('password-list.txt')
print(f)

f = open('password-list.txt', 'rt')
print(f)
print(f.readlines())
print(f.readlines()) #output is [] because the file has been read

f.seek(0) #change the file read position to start of the file
print(f.readlines())

f.seek(0)
for line in f:
    print(line.strip())
f.close()

f = open("test.txt", "a")
f.write("test line!")
f.close()

#get file handle property
print(f.name)
print(f.closed)
print(f.mode)

print("------")
with open("rockyou.txt", encoding='latin-1') as f:
    for line in f:
        pass