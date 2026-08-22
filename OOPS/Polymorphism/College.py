#College.py<---File Name Acts As Module Name
from Univ import Univ
class College(Univ):
    def getdata(self):
        self.cname=input("Enter College Name: ")
        self.cloc=input("Enter College Location: ")
        super().getdata()
    def dispdata(self):
        print("-"*50)
        print("College Details")
        print("-"*50)
        print("College Name:",self.cname)
        print("College Location:",self.cloc)
        print("-"*50)