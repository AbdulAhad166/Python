#Program for Reading list of +ve values and find  their squares from keyboard
print("Enter List of Values Separated by Commas: ")
d={float(val):float(val)**2 for val in input().split(',') if float(val)>0}
print(d)

