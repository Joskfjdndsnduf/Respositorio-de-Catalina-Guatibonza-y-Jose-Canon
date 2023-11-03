import numpy as np




#m=np.array([[1,2,-1],[1,0,1],[4,-4,5]])

#q=np.array([[1,1,1]])


#m=np.array([[3,2,4],[2,0,2],[4,2,3]])
#q=np.array([[4,3,6]])

m=np.array([[4,1],[0,4]])
q=np.array([[1,2]])
def multi(m,vp):
    c1=len(m[0])
    f2=len(vp)

    if c1!=f2:
        print("las matrices no se pueden multiplicar")
    else:
        f1=len(m)
        c2=len(vp[0])
        r=np.zeros(shape=(f1,c2))

        for i in range(f1):
            for j in range(c2):
                for k in range(c1):
                    r[i][j]+=m[i][k]*vp[k][j]
        return r


def mew(q,m):
    a=multi(m,q)

    b= multi(np.transpose(q),a)
    return b

def potmax(m,q):
    for i in range(10):
        if len(q)==1:
            c=np.transpose(q)
            z=multi(m,c)
            h=np.transpose(z)
            q=z/np.sqrt(multi(h,z))
            j=mew(q,m)
        else:
            z=multi(m,q)
            h=np.transpose(z)
            q=z/np.sqrt(multi(h,z))
            j=mew(q,m)
    return j,q

#print(potmax(m,q))

def potmin(m,q):
    for i in range(10):
        a=np.linalg.inv(m)
        if len(q)==1:
            c=np.transpose(q)
            z=multi(a,c)
            h=np.transpose(z)
            q=z/np.sqrt(multi(h,z))
            j=mew(q,a)
        else:
            z=multi(a,q)
            h=np.transpose(z)
            q=z/np.sqrt(multi(h,z))
            j=mew(q,a)
    return j,q
#Los vectores propios son q
print(potmin(m,q),potmax(m,q))

    