class Sun:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        
    def gives_water(self):
        print("Earth gives water.")
        
        
class Earth(Sun):
    def __init__(self, name, pressure):
        Sun.__init__(self, name, types="Earth")
        self.pressure = pressure
        
    def gives_water(self):
        print("Gravitional force is present!!")
        

d = Earth("Earth", "pressure")
d.gives_water()

a = Sun("Earth", "Mars")
a.gives_water()