#Program for accepting List of Numerical Integer Values and Multiple by 3 and 5 using filter()
print("Enter List of Values Separated By Comma:\n ")
lst=[int(val) for val in input().split(",") if int(val)>1]
print("Given Values= ",lst)
mult=list(filter(lambda x:x%3==0 and x%5==0,lst))
print("Multiples of 3 and 5= ",mult)