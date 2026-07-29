#Program for Getting all +VER Values
#Set comprehension
lst=[10,-20,30,-40,50,-60,70,-80,90]
pslist={val for val in lst if val>0}
nglist={val for val in lst if val<0}
print("List of +VE Values= ",pslist)
print("List of -VE Values= ",nglist)