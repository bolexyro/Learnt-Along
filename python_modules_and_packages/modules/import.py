# import <module_name>
# The simplest form is the one already shown above:

# import <module_name>
# Note that this does not make the module contents directly accessible to the caller. 
# Each module has its own private symbol table, 
# which serves as the global symbol table for all objects defined in the module. 
# Thus, a module creates a separate namespace.

# The statement import <module_name> only places <module_name> in the caller’s symbol table. 
# The objects that are defined in the module remain in the module’s private symbol table.

# From the caller, objects in the module are only accessible when prefixed with <module_name> via dot notation
# except if those objects are prefixed with an underscore which makes them private

# After the following import statement, mod is placed into the local symbol table. 
# Thus, mod has meaning in the caller’s local context:

import mod
print(mod)

# An alternate form of the import statement allows individual objects from the module to be imported directly into the caller’s symbol table:

# from <module_name> import <name(s)>
# Following execution of the above statement, <name(s)> can be referenced in the caller’s environment without the <module_name> prefix:

from mod import s
print(s)

# Following execution of the above statement, 
# <name(s)> can be referenced in the caller’s environment without the <module_name> prefix:

# It is even possible to indiscriminately import everything from a module at one fell swoop:

# from <module_name> import *
# This will place the names of all objects from <module_name> into the local symbol table, 
# with the exception of any that begin with the underscore (_) character.

# This indiscriminate import is not advised in large projects. Unless you know them all well and can be confident there won’t be a conflict, 
# you have a decent chance of overwriting an existing name inadvertently aka accidentally

# It is also possible to import individual objects but enter them into the local symbol table with alternate names
# This makes it possible to place names directly into the local symbol table but avoid conflicts with previously existing names:


# from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]

from mod import a as alist
print(alist)

# You can also import an entire module under an alternate name:
import mod as alt_mod
print(alt_mod.s)

# Module contents can be imported from within a function definition. In that case, the import does not occur until the function is called:

def bar():
    # allowed
    from mod import foo

    # python 3 doesn't allow the indiscriminate import * syntax from within a function:
    # from mod import *
    foo('corge')

bar()