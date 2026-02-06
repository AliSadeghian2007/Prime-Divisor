def is_prime(num):
    if num<2:
        return False
    if num==2:
        return True
    k=True
    for i in range (2,num):
        if num %i==0:
            k=False
    if k==False:
        return False
    else:
        return True

def count_prime_Divisor(n):
    count=0
    for i in range (1,n+1):
        if n%i==0:
            x=is_prime(i)
            if x==True:
                count+=1
        return count
