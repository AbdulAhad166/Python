#Program for demonstrating Positional Arguments
#This program is to show the importance of positional Arguments and these should be defined first only
def dispstudinfo(sno,sname,marks):
    print("\t{}\t{}\t{}".format(sno,sname,marks))
#Main Program
print("--------------------------------------")
print("\tSNo\tSName\tMarks")
print("--------------------------------------")
dispstudinfo(10,"RS",55.55)  #Function call with 3 positional Arguments
dispstudinfo(20,"TR",45.64)  #Function call with 3 positional Arguments
dispstudinfo(30,"RD",56.34)  #Function call with 3 positional Arguments
dispstudinfo(40,"BB",60.66)  #Function call with 3 positional Arguments
dispstudinfo(sname="BR",marks=46.44,sno=50)    #Function call with 3 keyword Arguments
dispstudinfo(60,marks=55.54,sname="RT")   #Function call with 1 pos and 3 keyword Arguments
#dispstudinfo(marks=67.87,sname="KT",70)
# #This will give SyntaxError: positional argument follows keyword argument
