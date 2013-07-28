# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Iterating maps

# <markdowncell>

# Let's think about how to iterate maps. Let's take a well-known map, $x \mapsto 2x (\text{mod} 1)$:

# <codecell>

f = lambda(x): 2*x if x<0.5 else 2*x-1

# <codecell>

%matplotlib inline
%config InlineBackend.figure_format = "svg"
from matplotlib import pyplot as plt
import numpy as np

# <codecell>

x = np.linspace(0, 1, 1000)

# <codecell>

ff = np.vectorize(f)

# <codecell>

plt.plot(x, ff(x))
plt.axis('scaled')

# <codecell>

def composition(g, f):
    return lambda(x): g(f(x)) 

# <codecell>

composition(ff, ff)

# <codecell>

ff2 = composition(ff, ff)

# <codecell>

plt.plot(x, ff2(x))
plt.plot(x, x)
plt.axis('scaled')

# <markdowncell>

# Let's generalise this to nth iterates:

# <codecell>

def iterate(f, n):
    """nth iterate of f"""

    if n == 0:
        return lambda(x): x  # identity
    
    if n == 1:
        return f
    
    # n > 1:
    return composition(f, iterate(f, n-1))
    
    

# <codecell>

iterate(ff, 2)

# <codecell>

plt.plot(x, iterate(ff, 5)(x))
plt.plot(x, x)
plt.axis('scaled')

# <markdowncell>

# What about other kinds of functions?

# <codecell>

@np.vectorize
def logistic(x):
    return 3.5*x*(1-x)

# <codecell>

plt.plot(x, iterate(logistic, 1)(x))
plt.plot(x, iterate(logistic, 2)(x))

plt.plot(x, iterate(logistic, 3)(x))
plt.plot(x, x)
plt.axis('scaled')

# <codecell>

import sympy
from sympy import init_printing
init_printing()

# <codecell>

x = sympy.symbols("x")
r = sympy.symbols("r")

# <codecell>

logistic = sympy.Lambda(x, r*x*(1-x))
logistic

# <codecell>

root = sympy.solve(logistic(x)-x, x)[1]
root

# <codecell>

sympy.diff(logistic(x), x)

# <codecell>

_.subs({x:root})

# <codecell>

sympy.simplify(_)

# <codecell>


