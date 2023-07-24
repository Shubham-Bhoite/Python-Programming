# We can use class Method as a constructor alternative

class StudentData:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    
    def showDetails(self):
        print(f"Student {self.name} is from {self.branch} Branch")
    
    @classmethod
    def stringSplitter(cls,string):
        return cls(string.split("/")[0],string.split("/")[1])

string="Shubham/CSE"
std1=StudentData.stringSplitter(string)
std1.showDetails()
