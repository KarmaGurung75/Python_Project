'''
def outer_function():
    a=20
    def inner_func():
        a=30
        print("inner:",a)
    inner_func()
    print("a",a)

a=10
outer_function()
print("a:",a)
'''
'''
def outer_function():
    global a
    a = 20

    def inner_func():
        global a
        a = 30
        print("inner:", a)

    inner_func()
    print("outer a", a)


a = 10
outer_function()
print("Global a:", a)
'''
def greeter(name):
    print("Good morning")
    print("Hello " + str(name))
name="Metthew"
greeter("world")
