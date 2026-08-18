#Employee.py<---File Names Acts as Module
class Employee:
    def __init__(self,eno,name,sal):
        self.eno=eno
        self.name=name
        self.sal=sal
    def dispempdata(self):
        print("\t{}\t\t{}\t\t{}".format(self.eno,self.name,self.sal))