# Importing still works the same as shown previously. 
# Syntax is similar, but additional dot notation is used to separate package name from subpackage name:

from pkg_I.sub_pgk_I.mod1 import foo
print(dir())
foo()

from pkg_I.sub_pkg_II import mod3