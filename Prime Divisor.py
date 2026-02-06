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

def main ():
    number=int(input("How many number do you want to test?"))
    max=-1
    Answer=[]
    ls=list(map(int,input().split()))
    for i in range (number):
        Answer.append(count_prime_Divisor(ls[i]))
    for j, n in enumerate(Answer):
        if n>max:
            max=n
            index=j
        elif n==max:
            if ls[j]>ls[index]:
                max=n
                index=j
    print(f"{ls[index]} {Answer[index]}")
if __name__=="__main__":
    main()