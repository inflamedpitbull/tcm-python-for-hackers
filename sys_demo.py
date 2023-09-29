import sys
import time

print(sys.version)
print(sys.executable)
print(sys.platform)


for i in range(1,5):
    sys.stdout.write(str(i))
    sys.stdout.flush() #flush out all the buffer to the terminal

for i in range(1,5):
    print(i)

for i in range(0,51):
    time.sleep(0)
    sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(50-i)))
    sys.stdout.flush()
    sys.stdout.write("\n")


print(sys.argv)

if len(sys.argv) != 3: 
    print("[X] To run {} enter an username and password.".format(sys.argv[0]))
    sys.exit(5)
else:
    username = sys.argv[1]
    password = sys.argv[2]
    print("{} {}".format(username, password))
    

print(sys.path)
print(sys.modules)

sys.exit(0)