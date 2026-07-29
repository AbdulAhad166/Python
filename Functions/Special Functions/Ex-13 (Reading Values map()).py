#Program for reading the values from keyboard by using map()
print("Enter List of Values Separated By Comma: ")
lst=tuple(map(int,input().split(",")))
print("List of Values= ",lst)