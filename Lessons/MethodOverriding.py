# Allows you to redefine a method in derived class.

class funds:
  def __init__(self, a, b):
    self.a = a
    self.b = b
    
  def addition(self):
      return self.a + self.b

class income(funds):
    def __init__(self, GST):
      self.GST = GST
      super().__init__(GST, GST)

tally = income(200)
print(tally.addition())
