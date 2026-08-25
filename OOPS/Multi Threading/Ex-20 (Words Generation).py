#Program for Accepting a Line of Text and Display Every Word  By using Therads after each and every Second
import threading,time
class Line:
    def getline(self):
        self.line=input("Enter A Line Of Text: ")
    def generate(self):
        self.getline()   #Calling the Instance Method
        print("Give Line of Text: ",self.line)
        words=self.line.split()
        for word in words:
            print("\t {}".format(word))
            time.sleep(1)
#Main Program
t1=threading.Thread(target=Line().generate)
t1.start()