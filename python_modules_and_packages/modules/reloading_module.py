# For reasons of efficiency, a module is only loaded once per interpreter session. 
# That is fine for function and class definitions, which typically make up the bulk of a module’s contents. 
# But a module can contain executable statements as well, usually for initialization. 
# Be aware that these statements will only be executed the first time a module is imported.

import mod # this would cause every statement in the mod to run
from mod import * # statement won't be run since they've been run before. Statements won't be executed on subsequent imports

# To force reload a module
import importlib
importlib.reload(mod)
import mod