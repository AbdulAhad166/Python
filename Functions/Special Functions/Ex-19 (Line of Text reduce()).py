#Program for accepting List of words and convert into single line of text with reduce()
import functools
lst=list(map(str,input("Enter List of Words Separated By Comma: ").split(",")))
res=functools.reduce(lambda x,y:x+" "+y,lst)
print("Line of Text= ",res)