#Number Pattern – Increasing
n=int(input('enter a number= '))
for i in range(1,n+1):
    print(' ',end=' ')
    for j in range(1,i+1):
        print(i,end=' ')
    print()
