# Program for finding Max and Min from List of Elements
# without using max() and min()

def readvals():
    n = int(input("Enter How many values do you want: "))
    if n <= 0:
        return []          # Returning an empty list
    else:
        lst = []
        for i in range(1, n + 1):
            val = float(input("Enter {} Value: ".format(i)))
            lst.append(val)
        return lst
def findmax(lst):
    if len(lst) == 0:
        print("\tList is Empty ---> Can't Find Max Element")
    else:
        mv = lst[0]               # Assume first element is maximum
        for val in lst[1:]:       # Check remaining elements
            if val > mv:
                mv = val
        print("\tMax = {}".format(mv))
def findmin(lst):
    if len(lst) == 0:
        print("\tList is Empty ---> Can't Find Min Element")
    else:
        mv = lst[0]               # Assume first element is minimum

        for val in lst[1:]:       # Check remaining elements
            if val < mv:
                mv = val

        print("\tMin = {}".format(mv))
# Main Program
vals = readvals()
findmax(vals)
findmin(vals)



