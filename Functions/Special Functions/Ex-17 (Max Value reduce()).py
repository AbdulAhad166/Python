#Program for accepting List of Numerical Values and find max() using reduce()
import functools
lst=list(map(int,input("Enter List of Values Separated By Comma: ").split(",")))
maxvalue=functools.reduce(lambda x, y:x if x > y else y, lst)
print("Max Value= ", maxvalue)