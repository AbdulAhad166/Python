#Program for counting the notes of money from ATM
w=int(input("Enter your Withdraw Amount: "))
n500=w//500
w=w%500
n200=w//200
w=w%200
n100=w//100
w=w%100
print("\t Number of Rs 500:{}".format(n500))
print("\t Number of Rs 200:{}".format(n200))
print("\t Number of Rs 100:{}".format(n100))