#Program for accepting Odd +Ve Numbers using filter()
print("Given List of Values Separated By Comma: ")
lst=[int(val) for val in input().split(",")]
print("Given Values= ",lst)
odd=list(filter(lambda x:x%2!=0 and x>0,lst))
print("Odd Numbers= ",odd)