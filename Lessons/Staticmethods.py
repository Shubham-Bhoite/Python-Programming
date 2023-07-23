# Methods that belong to class rather than instance of class
# Need to give @staticmethod before declaring method

class Math:
    @staticmethod
    def divide(a, b):
        return a / b

result = Math.divide(15, 5)
print(result) 