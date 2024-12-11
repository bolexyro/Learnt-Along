
# # if the pkg directory resides in a location where it can be found (in one of the directories contained in sys.path), 
# # you can refer to the two modules

# # NB: The whole reloading thing talked about in modules/reloading_module.py also applies to packages
# # from pkg import mod1
# # import pkg.mod2

# # print(dir())

# # mod1.foo()
# # pkg.mod2.bar()


# # Now when the package is imported, the global list A is initialized:
# # import pkg
# # print(f'global list A is {pkg.A}')

# import pkg
# # import pkg.mod1
# print(dir())
# print(pkg.mod1.foo())
# print(pkg.bar())


# # When you import a package (e.g., import pkg1), 
# # Python only executes the code in the package's __init__.py file. 
# # It doesn’t automatically import the modules within the package unless explicitly specified in __init__.py.

# # import pkg1
# # You cannot directly access module1 or module2 like pkg1.module1 because they haven’t been imported into the package namespace.

# # You can modify the __init__.py file to automatically import specific modules or symbols when the package is imported.

# # To access module1, you need to:

# # 1. Import it explicitly:
# # import pkg1.module1
# # 2. Or access it via the __init__.py file 

# # __init__.py
# # from . import module1
# # from . import module2

# # import pkg1
# # You can access module1 and module2 as:


# # pkg1.module1.some_function()
# # pkg1.module2.some_other_function()

# # Why This Behavior Exists
# # Performance: Importing only the __init__.py keeps the initial package import lightweight, especially for large packages with many modules.
# # Explicit Control: You can decide which modules or functions to expose at the package level by selectively importing them in __init__.py.

# # This behavior doesn't apply to modules tho
# # When you import  module, python executes the entire file (module1.py) and makes all the objects 
# # (functions, classes, variables) defined in it available under the module's namespace.


# # SUMMARY
# # When you import a package, only the contents, objects defined of __init__.py are included in the package's namespace.
# # To add modules or objects to the package namespace, you must explicitly import them in __init__.py.

# from pkg.mod2 import bar
# bar()


# this wildcard import imports all the objects available in the name space of the package (typically defined in __init__.py).
# If __init__.py file includes an __all__ list, only the modules or objects in that list will be imported with the wildcard.
from pkg import *
# mod2.bar()
print(dir())
# This __all__ list provides the capability to disallow this wildcard import, simply by setting __all__ = []
# __all__ can be defined in a module as well and serves the same purpose: to control what is imported with import *.