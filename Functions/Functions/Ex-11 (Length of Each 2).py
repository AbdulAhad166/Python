#Program for Finding Length of each word in list
#Dict Comprehension 2
lst=['PYTHON','JAVA','ROSSUM','HYDERABAD','NETHERLANDS']
d={val:len(val) for val in lst}
print(d)