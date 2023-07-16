#Default arguments
def name(fname, mname = "Shrikant ", lname = "Thackeray"):
    print("Jay Maharashtra,", fname, mname, lname)

name("Raj")


#Keyword arguments
def name(fname, mname, lname):
    print("Namaste,", fname, mname, lname)

name(mname = "Prasadrao", lname = "Tanpure", fname = " Prajakt")


#Required arguments
def name(fname, mname, lname):
    print("Mere Bhai aur Bahano,", fname, mname, lname)

name("Narendra", "Damodardas", "Modi")


#Variable-length arguments
def name(*name):
    print("Hey Coder,", name[0], name[1], name[2])

name("Prashant", "Kantilal", "Jagtap")


#return Statement
def name(fname, mname, lname):
    return "Only Rashtrawadi, " + fname + " " + mname + " " + lname

print(name("Sharad", "Govindrao", "Pawar"))