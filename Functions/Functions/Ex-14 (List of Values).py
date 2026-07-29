#Program for Reading List of Values from Key Board
#List Comprehension
lst=[  float(val)  for val in input("Enter List of Values separated by Space:\n").split()  ]
print("Content of List=",lst)