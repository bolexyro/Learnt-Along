# The built-in function dir() returns a list of defined names in a namespace. 
# Without arguments, it produces an alphabetically sorted list of names in the current local symbol table

import mod
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'mod']
from mod import *
print(dir())
# ['Foo', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'foo', 'mod', 's']