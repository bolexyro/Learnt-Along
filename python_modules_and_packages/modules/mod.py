# A module is a single Python file that contains code, such as functions, 
# variables, and classes, which can be reused in other Python programs.

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

# When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module.
# However, if a file is run as a standalone script, 
# __name__ is (creatively) set to the string '__main__'. 
# Using this fact, you can discern which is the case at run-time and alter behavior accordingly:

print(__name__)

# To distinguish between when a file is loaded as a module and when it is run as a standalone script?
if __name__ == "__main__":
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)