import inauguralproject
import numpy as np
import math 
from scipy import optimize
%matplotlib inline 
import matplotlib.pyplot as plt

m = 1
v = 10
e = 0.3
t_0 = 0.4
t_1 = 0.1
k = 0.4

def obj(c,l,v,e):
    return np.log(c) - v*(l**(1+1/e))/(1+1/e)
    
def u(l,m,w,v,e,t_0,t_1,k):
    c = m + w*l-(t_0*w*l + t_1*max(w*l-k,0))
    return -obj(c,l,v,e)

def opt(w,m,v,e,t_0,t_1,k):
    sol = optimize.minimize_scalar(u,bounds=(0,1),args=(w,m,v,e,t_0,t_1,k))
    l = sol.x
    c = m + w*l +(t_0*w*l + t_1*max(w*l-k,0))
    return [c,l]

ls = []
cs = []
n = 10000
ws = np.linspace(0.5,1.5,n)
for i in ws:
    opt_value = opt(i,m,v,e,t_0,t_1,k)
    cs.append(opt_value[0])
    ls.append(opt_value[1])

fig = plt.figure(figsize=(10,4))
ax_left = fig.add_subplot(1,2,1)
ax_left.plot(ws,cs,color='Blue')

ax_left.set_title('optimal c relate to w')
ax_left.set_xlabel('w')
ax_left.set_ylabel('optimal c')
ax_left.grid(True)

ax_right = fig.add_subplot(1,2,2)
ax_right.plot(ws,ls,color='Red')

ax_right.set_title('optimal l relate to w')
ax_right.set_xlabel('w')
ax_right.set_ylabel('optimal l')
ax_right.grid(True)

def tax_rev(w,m=1,v=10,e=0.3,t_0=0.4,t_1=0.1,k=0.4):
    T = 0 
    for i in ws:
        opt_value = opt(i,m,v,e,t_0,t_1,k)
        l_0 = opt_value[1]
        T += t_0*i*l_0 + t_1*max(i*l_0-k,0)
    return T
print("tax revenue" + " " + str(tax_rev(i)))

def new_tax_rev(w,m=1,v=10,e=0.1,t_0=0.4,t_1=0.1,k=0.4):
    T = 0
    for i in ws:
        opt_value = opt(i,m,v,e,t_0,t_1,k)
        l = opt_value[1]
        T += t_0*i*l + t_1*max(i*l-k,0)
    return T
print ("tax revenue" + " " + str(tax_rev(i)))

def opt_tax_rev(x,w,m=1,v=10,e=0.3):
    t_0 = x[0]
    t_1 = x[1]
    k = x[2]
    T = 0
    for i in ws:
        opt_value = opt(i,m,v,e,t_0,t_1,k)
        l = opt_value[1]
        T += t_0*i*1_0 + t_1*max(i*1_0-k,0)
    return T

initial_guess=[0,0,0]
bounds = ((0,1),(0,1),(0,1))
sol = optimize.minimize(opt_tax_rev,initial_guess,method='SLSQP',bounds = bounds, args=(i,m,v,e))

t0_opt = sol.x[0]
t1_opt = sol.x[1]
k_opt = sol.x[2]

print ("optimal t_0"+ " " + str(t0_opt))
print ("optimal t_1"+ " " + str(t1_opt))
print ("optimal k" + " " + str(k))
