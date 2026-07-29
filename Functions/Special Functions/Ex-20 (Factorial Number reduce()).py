#Program for calculating Factorial of a Number using reduce()
import functools
fact=functools.reduce(lambda x,y:x*y,range(1,int(input("Enter Any Number: "))+1))
print("Factorial=",fact)