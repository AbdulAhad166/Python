#Program for accepting List of Numerical Values and find min() with reduce()
import functools
lst=list(map(int,input("Enter List of Values Separated By Comma: ").split(",")))
res=functools.reduce(lambda x,y:x if x<y else y,lst)
print("Min Value= ",res)