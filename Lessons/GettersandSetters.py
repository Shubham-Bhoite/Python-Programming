#Getters-->
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
obj = MyClass(10)
obj.value
10


#Getters and Setters-->
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        
obj = MyClass(10)
obj.value = 20
obj.value
20

#Example :
class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 55
print(obj.ten_value)
obj.show()
