# If a file named __init__.py is present in a package directory, 
# it is invoked when the package or a module in the package is imported. 
# This can be used for execution of package initialization code, 
# such as initialization of package-level data.


# __name__ here is the name of package which in this case is pkg

print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']

# __init__.py can also be used to effect automatic importing of modules from a package. 
# For example, the statement import pkg only places the name pkg in the caller’s local symbol table and doesn’t import any modules. 
# But if __init__.py in the pkg directory contains the following:

# import pkg.mod1, pkg.mod2
from . import mod1
from .mod2 import bar

# Python follows this convention: if the __init__.py file in the package directory contains a list named __all__, 
# it is taken to be a list of modules and objects that should be imported when the statement from <package_name> import * is encountered.

__all__ = ["mod1", "A"]
