#Program for Extract the mail id s from given file where It contains Text Data
import re
try:
	with open("C:\\Users\\dell\\PycharmProjects\\Python\\OOPS\\mails.data","r") as fp:
		filedata=fp.read()
		sp1="[A-Z][a-z]+"
		sp2=r"\S+@\S+"
		nameslist=re.findall(sp1,filedata)
		mailslist=re.findall(sp2,filedata)
		print("----------------------------------------------------------")
		print("\tName\t\tMail-ID")
		print("----------------------------------------------------------")
		for names,mail in zip(nameslist,mailslist):
			print("\t{}\t\t{}".format(names,mail))
		print("----------------------------------------------------------")
except FileNotFoundError:
	print("File Does Not Exist")