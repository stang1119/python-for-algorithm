def  tryit(i):    #  search and backtrack routine 
    global  sn, a, b, c, x
    for  j  in range(8) :
        if  a[j] and b[i+j] and c[i-j+7] :
            x[i]=j+1
            a[j]=0
            b[i+j]=0
            c[i-j+7]=0
            if  i<7 :
                tryit(i+1)
            else :
                sn+=1  # count the solution 
                print(" Solution %2d: %s" % (sn,x) )
            a[j]=1
            b[i+j]=1
            c[i-j+7]=1
x=[None]*8    # queen position in the i-th column 
a=[1]*8        # queen occupies the i-th row 
b=[1]*15     # queen occupies the right diagonal 
c=[1]*15     # queen occupies the left diagonal 
sn=0     # solution counter 
tryit(0)
print(" Total solutions: %d\n" % sn)
