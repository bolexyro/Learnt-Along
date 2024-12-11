import mod # the name of file we are importing
# When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled from the following sources:

# The directory from which the input script was run or the current directory if the interpreter is being run interactively

# The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for PYTHONPATH is OS-dependent 
# but should mimic the PATH environment variable.)

# An installation-dependent list of directories configured at the time Python is installed

# The resulting search path is accessible in the Python variable sys.path, which is obtained from a module named sys:
# import sys
# print(sys.path)

# if the mod.py file is not in any of these 3 directories, but is in another directory, but you still want to use it here,
# what you can do is to modify the sys.path at run-time so that it contains that directory
# sys.path.append(r'C:\Users\john')


print(mod.s)
print(mod.a)
mod.foo('Hello')
print(mod.Foo())

# Once a module has been imported, you can determine the location where it was found with the module’s __file__ attribute:
print(mod.__file__)