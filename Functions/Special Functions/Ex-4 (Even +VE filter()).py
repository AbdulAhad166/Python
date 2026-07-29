#Program for accepting even +VE Numbers using fliter()
print("Enter List of Values Separated By Space:\n ")
lst=[int(val) for val in input().split()]
print("Given Values= ",lst)
even=list(filter(lambda x:x%2==0 and x>0,lst))
print("Even Numbers= ",even)