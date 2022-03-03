import matplotlib.pyplot as plt
import scipy.integrate 
import numpy as np


def x_i(i,n):
    return 2*i / n; 

# za funkcje bazową przyjmujemy 
#e_i = {x - x_i-1/x_i-x_i-1 , x należy do (x_i-1,x_i),  
#       x_i+1- x / x_i+1-x_i , x należy do (x_i,x_i+1) }
# wiemy, że x_i+1-x_i  =  x_i - x_i-1 =  h = 2/n 



def e(i,x,n):
    if x >= x_i(i-1,n) and x <= x_i(i,n):
        return (x-x_i(i-1,n))/(2/n) 
    elif x >x_i(i,n) and x <= x_i(i+1,n):
        return (x_i(i+1,n)-x)/(2/n) 
    else: 
        return 0
    
    
#pochodna e
def e_prim(i,x,n):
    if x >= x_i(i-1,n) and x <= x_i(i,n):
        return n/2
    elif x >x_i(i,n) and x <= x_i(i+1,n):
           return -n/2
    else: 
        return 0
    

def L(i,n):
   return -20*e(i,0,n)
    
def B(i,j,n):
    # szukamy przedziałów całkowania
    a = 0
    b = 2

    if abs(i-j) <= 1:
        if i >= j:
            a = max(a,x_i(i-1,n))
            b = min(b,x_i(j+1,n))
        else:
            a = max(a,x_i(j-1,n))
            b = min(b,x_i(i+1,n))
        
        return scipy.integrate.quad(lambda x : e_prim(i,x,n)*e_prim(j,x,n),a,b)[0]-e(i,0,n)*e(j,0,n)
    else:
        return 0
  


def find_soltion(n):
    #obliczamy odległość pomiędzy kolejnymi punktami
    h = 2 / n
    
    A = [] #macierz dla B(u,v)
    G = [] #macierz dla L(v)
    
    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append(B(j,i,n))
        G.append(L(i,n))
    

    U = np.linalg.solve(A,G)
    
    Results = [0]*200
    
    #obliczanie wartości dla funkcji
    for i in range(200):
        suma = 0 
        for j in range(len(U)):
            suma = suma + U[j]*e(j,x_i(i,200),n)
        Results[i] = suma
 
   
    set_X = np.linspace(0,2,200)
    
    plt.title("Wykres aproksymacji funckji y = u(x)")
    plt.plot(set_X, Results)
    plt.show()

    
    
    
find_soltion(50)