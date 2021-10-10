from math import sqrt
def is_prime(num):
    for i in range(2, int(sqrt(num)) + 2):
        if (num % i) == 0 and num !=2:
             flag = True
             break
        else:
            flag = False
    return flag

l = []
n = int(input("enter the number for checking"))

for i in range(2,int(sqrt(n)) + 2):
    if n % i == 0 :
         check = is_prime(i)
         if check == False :
                l.append(i)

z = len(l)
print("given is a", z ,"way prime number")
print(l)

