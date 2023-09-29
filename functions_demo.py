def function1():
    print("heelo from functions!")

function1()

def function2():
    return "hello from function2!"

return_from_function2 = function2()
print(return_from_function2)

def function3(s):
    print("\t{}".format(s))

function3("parameter")

def function4(s1,s2):
    print("{} {}".format(s1,s2))

function4("any","thing")
function4(s1="thing",s2="any")
function4(s2="thing",s1="any")

def function5(s1 = "default"):
    print("{}".format(s1))

function5()
function5("anything")

def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("function6","a","b")

def function7(**ks):
    for a in ks:
        print(a, ks[a])

function7(a="1",b="2",c="3")

def function8(s,f,i,l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("stiring", 1.0, 1, ['l','i','s','y'])

v=100


def function9():
    global v #modified global var
    v=200
    print(v)
function9()
print(v)

def function10():
    print("hello from function10")

def function11():
    function10()
    print("hello from function11")
function11()

def function12(x):
    print(x)
    if x > 0:
        function12(x-1)

function12(5)

def function13(x):
    while x>=0:
        print(x)
        x -=1
function13(5)
    
