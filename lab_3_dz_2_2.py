import numpy as np

T = 200
E = 300
k = 1.380662*10**(-23)
e = 2.71828
h = 6.626*10**(-34)
np.pi = 3.14

N = (2/(np.sqrt(np.pi)))*(h/((k*T)**(3/2)))*(e**((-E)/(k*T)))*(E**(T/2))
                        

print(N)
