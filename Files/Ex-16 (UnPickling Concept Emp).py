#Program for Reading Record from the File of Secondary Memory
#by using Un-Pickling Concept
def loadrecord():
    import pickle
    with open("emp.pick", "rb") as fp:
        while True:
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t {}".format(val),end="\t")
                print()
            except EOFError:
                print("End Of File")
                break
#Main Program
loadrecord() #Function Call