for j in range(1,10):
    pass
    for i in range(j,10):
        print("%d*%d=%d" % (j,i,j*i),end="\t")
    print("")
    
for num in range(1,10):
    for x in range(1,num+1):
        print("%d*%d=%d" % (x,num,x*num),end="\t");
    print("")
