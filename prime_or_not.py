n = 3
def prime(n):


    if n ==1:
        print ("not a prime")
for d in range(2, n):
    if n % d==0:
        print ("not a prime")
        break
    else:
        print("it is a prime")


