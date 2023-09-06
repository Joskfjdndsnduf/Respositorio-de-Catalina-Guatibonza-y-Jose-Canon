x=np.linspace(0,3,3)

def func(x):
    return ((np.e)**-x)-x

y=func(x)
print(y)
h=x[1]-x[0]

def InterpolacionNewton(X,Y,x):
    
    sum_ = Y[0]
    
    Diff = np.zeros(( X.shape[0],Y.shape[0] ))
    h = X[1]-X[0]
    
    Diff[:,0] = Y

    poly = 1.
    
    for i in range(1,len(X)):
        
        poly *= (x-X[i-1])
        
        for j in range(i,len(X)):
            
            Diff[j,i] = Diff[j,i-1] - Diff[j-1,i-1] 
    
        sum_ += poly*Diff[i,i]/(np.math.factorial(i)*h**(i))
        
    return sum_
t=np.linspace(-7,6,20)
I=InterpolacionNewton(x,y,t)
plt.scatter(t,I)
plt.show()