def foo():
    # A module in the package can access the global variable declared in __init__.py by importing it in turn:
    from pkg import A
    print('[mod1] foo() / A = ', A)

class Foo:
    pass