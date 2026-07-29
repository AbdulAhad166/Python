#Program for Finding Length of particular word in list
#Dict Comprehension 1
lst=['PYTHON','JAVA','GUIDO','HYDERABAD','NETHERLANDS']
d={val:len(val) for val in lst if val.startswith('HYDERABAD')}
print(d)