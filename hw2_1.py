Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format("Bytes","Largest Unsigned Int","Minimum Signed Int","Maximum Signed Int"))
for i in range(1,9):
    #print(i)
    n=i*8
    
    total=0

    while (n>0):
        n=n-1
        total=total+2**n
    max_si=(total-1)//2
    #max_si=round(max_si)
    min_si=((total+1)//2)*-1
    #min_si=round(min_si)
            
    #print(total)
    print(Table.format(i,total,min_si,max_si))