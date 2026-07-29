#Program for accepting List of primes +ve numbers using filter()
def isprime(n):
    res=True
    for i in range(2,n):
        if n%i==0:
            return False
            break
    return res
#Main Program
print("Enter List of Values Separated by Comma:\n ")
lst=[int(val) for val in input().split(",")]
print("Given Values= ",lst)
#We need to convert to lst,set,tuple
prime=list(filter(isprime,lst))
print("Prime Numbers= ",prime)
