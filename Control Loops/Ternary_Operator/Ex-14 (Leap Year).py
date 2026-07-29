#program to check whether a given year is a leap year using the if..else operator.
year=int(input("Enter the Year: "))
res="Leap Year" if year % 4 ==0 else "Not Leap Year"
print(res)