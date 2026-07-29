#Program for Demonstrating the Need of Local and Global Variables
lang="PYTHON" #Global Variable Here Global Variables can be used anywhere inside the function
              # outside the function but should be called before the function call
def learnAI():
    sub1="AI"
    print("To Implement '{}' Based Applications we need '{}' Programming Language".format(sub1,lang))
def learnML():
    sub2="ML"
    print("To Implement '{}' Based Applications we need '{}' Programming Language".format(sub2,lang))
#Main Program
learnAI()
learnML()