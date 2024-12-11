def baz():
    print('[mod3] baz()')

class Baz:
    pass

# a module in one subpackage can reference objects in a sibling subpackage 
# (in the event that the sibling contains some functionality that you need). 
# For example, suppose you want to import and execute function foo() 
# (defined in module mod1) from within module mod3. You can either use an absolute import:

from pkg_I.sub_pgk_I.mod1 import foo
foo()

# Relative path
# where .. refers to the package one level up. From within mod3.py, which is in subpackage sub_pkg2,/
# so .. would refer to pkg_I
from ..sub_pgk_I.mod2 import bar
bar()