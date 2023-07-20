# if "__ name__ == "__ main__" in Python

-  Before executing code, Python interpreter reads source file and define few special variables/global variables.

-  If the python interpreter is running that module (the source file) as the main program, it sets the special __ name __ variable to have a value __ main __. If this file is being imported from another module, __ name __ will be set to the module’s name. Module’s name is available as value to __ name __ global variable.

-  A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.