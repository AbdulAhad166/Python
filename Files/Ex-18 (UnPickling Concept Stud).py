#Program for Reading Record from the File of Secondary Memory
#by using Un-Pickling Concept
import pickle
def loadrecord():
    with open("stud.pick","rb") as fp:
        while True:
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t {}".format(val),end="\t")
                print()
            except EOFError:
                print("End of file")
                break
#Main Program
loadrecord()
