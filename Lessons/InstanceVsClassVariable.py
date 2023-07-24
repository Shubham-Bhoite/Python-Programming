# Class Variables defined outside to the class and shared among all methods belong to class
# Instance Variables defined atr instance level and are unique to each instance of class

class OrganizationData:
    OrgName="World Health Organization" # Class Variable
    def __init__(self,name,location):
        self.name=name
        self.id=222
        self.location=location # Instance Variable

    def ShowOrganizationDetails(self):
        print(f" ID No: {self.id} is {self.name} from {self.location} and organization is {self.OrgName}.")

cus1=OrganizationData("Shubham","Rahuri")
cus1. ShowOrganizationDetails()

cus2=OrganizationData("Varad","Pune")
cus2.OrgName="CID" # Not Necessary to change
cus2.location="pune"
cus2.id=444
cus2.ShowOrganizationDetails()