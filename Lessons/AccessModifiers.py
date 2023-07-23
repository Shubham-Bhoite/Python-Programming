# Public -->
# Can Be Accessed from anywhere
# Default Access Modifier 

# Private -->
# Only Accessible within class
# Private consider by double underscore(__)

# Protected -->
# It accessible with class and subclass
# Protected consider by single underscore(_)


class Animals:
    def __init__(self):
        self._privateAtr="I am Private"
        self.__mangledAtr="I am Mangled"

s1=Animals()
print(s1._privateAtr)
print(s1._Animals__mangledAtr)
print(s1.__mangledAtr)
