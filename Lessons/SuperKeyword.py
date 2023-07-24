# super() keyword in python is used to refer to the parent class

class PrimeMinister:
    Nidhi = 500000
    def __init__(self,name,party,income):
        self.name=name
        self.party=party
        self.income=income
    
    def watchPM(self):
        print(f"The Prime Minister Name is {self.name} is a {self.party} party member.")
    
    def salaryCalc(self):
        return self.income+ self.Nidhi 
    
class MaharashtraCM(PrimeMinister):
    def __init__(self,name,party,payment,salary):
        self.name=name
        self.party=party
        self.payment=payment
        self.salary=salary
        super().__init__(name,party,payment)

    def watchPM(self):
        print(f"The CM Name is {self.name} is a {self.party} party member.")

    def totalpayment(self):
        return self.payment + super().salaryCalc()


minister=MaharashtraCM("Eknath Shinde","ShivSena",23000,500000)
minister.watchPM()
print("Total Payment received: ",minister.totalpayment())

