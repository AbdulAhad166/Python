#Program for Accepting List of Values and find their sum bu using reduce()
import functools
lst=list(map(float,input("Enter List of Values Separated By Comma: ").split(",")))
res=functools.reduce(lambda x,y:x+y,lst)
print("Sum= ",res)