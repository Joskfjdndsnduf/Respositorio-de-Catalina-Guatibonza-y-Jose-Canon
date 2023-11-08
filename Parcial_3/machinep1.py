

def f2(x,y):
    return x**4 + y**4 - 2*(x-y)**2

Dx = lambda f,x,y,h=1e-5: (f(x+h,y) - f(x-h,y))/(2*h)
Dy = lambda f,x,y,h=1e-5: (f(x,y+h) - f(x,y-h))/(2*h)

x0, y0 = 0,3

Gradient = lambda f,x,y: np.array([Dx(f,x,y),Dy(f,x,y)])
Gradient(f2,x0,y0)

def Minimizer(f, N = 100, gamma = 0.001):
    
    r = np.zeros((N,2))
    r[0] = np.random.uniform(-5.,5.,size=2)
    
    Grad = np.zeros((N,2))
    Grad[0] = Gradient(f,r[0,0],r[0,1])
    
    # We save the gradient in each step

    for i in range(1,N):
        r[i] = r[i-1] - gamma*Gradient(f,r[i-1,0],r[i-1,1])+0.6*(r[i-2]-r[i-3])
        Grad[i] = Gradient(f,r[i-1,0],r[i-1,1])
        
        
    return r,Grad