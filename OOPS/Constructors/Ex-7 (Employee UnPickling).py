#Program For Reading the File of Employee Data
import pickle
class EmployeeUnpick:
    def readempdata(self):
            try:
                with open('emp.pick', 'rb') as fp:
                    while True:
                        try:
                            emprecord=pickle.load(fp)
                            emprecord.dispempdata()
                        except EOFError:
                            break
            except FileNotFoundError:
                print("File Does Not Exist")
epo=EmployeeUnpick()
epo.readempdata()
