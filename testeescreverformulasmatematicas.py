from sympy.interactive import printing
printing.init_printing(use_latex= True)

import numpy as np
import sympy as sp

def f(x):
    return np.sin(x)

func = sp.Function('func')

x = sp.Symbol('x')

func = sp.sin(x)
print(func)

inte = sp.integrate(func,x)
print(inte)