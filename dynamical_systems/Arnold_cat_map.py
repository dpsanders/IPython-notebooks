# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Calculating and visualising the Arnold cat map

# <codecell>

%install_ext https://raw.github.com/minrk/ipython_extensions/master/nbtoc.py

# <codecell>

%load_ext nbtoc
%nbtoc

# <markdowncell>

# The Arnold cat map is a canonical example of a (uniformly) *hyperbolic* ("*chaotic*") area-preserving, or "Hamiltonian", dynamical system.
# In this notebook, we will construct figures showing the action of this map. To do so, we will use some computational geometry to manipulate
# line segments and polygons; in particular, it will be necessary to find their intersections.

# <codecell>

%matplotlib inline
%config InlineBackend.figure_format = "svg"

# <codecell>

import numpy as np
from Polygon_class import *

from matplotlib import pyplot as plt

# <codecell>

def norm(v):
    return np.sqrt(np.dot(v, v))

# <headingcell level=2>

# Simple computational geometry

# <markdowncell>

# It is first necessary to do define some simple concepts and functions from computational geometry.

# <headingcell level=3>

# Line segments

# <markdowncell>

# We first define an object to represent a
# directed line segment joining two points $\mathbf{p}_0$ and $\mathbf{p}_1$.

# <headingcell level=2>

# Mapping vertices and polygons

# <markdowncell>

# A *map* is a function
# $f : \mathbb{R}^2 \to \mathbb{R}^2.$ 
# Our first example is the map $\mathbf{x} \overset{f}{\mapsto} \mathsf{M} \cdot \mathbf{x}$, where
# 
# $$\mathsf{M} := \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}:$$

# <codecell>

M = np.array([[2, 1], [1, 1]])

f = lambda x: np.dot(M, x)

print M

# <markdowncell>

# `f` applies the map to a single vertex. Now we need something to apply it to all the vertices of a polygon, creating a new 
# polygon:

# <codecell>

def map_poly(f, poly):
    """Apply the map f to each vertex of the Poygon poly, returning a new Polygon"""
    
    vertices = poly.vertices
    new_vertices = [f(vertex) for vertex in vertices]
    
    return DirectedPolygon(new_vertices)

# <markdowncell>

# Let's apply our map `f` to the unit square, and then apply it again to get the second iterate $f^{(2)} := f \circ f$:

# <codecell>

unit_square = DirectedPolygon([(0.,0.), (1.,0.), (1.,1.), (0.,1.)])

iterates = [unit_square]

# <codecell>

iterates

# <markdowncell>

# Let us draw the original unit square and its first iterate:

# <codecell>

def draw_polygon(poly):
    plt.fill(poly.vertices[:,0], poly.vertices[:,1], alpha=0.5)

# <codecell>

draw_polygon(unit_square)


plt.axis('scaled')
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)

plt.grid()

plt.axis?

# <markdowncell>

# Let's make a function to calculate (if they are not already available)
# and draw higher iterates:

# <codecell>

def draw_iterates(n):
    """Draw iterates up to and including the nth"""
    
    while len(iterates) < n+1:
        iterates.append(map_poly(f, iterates[-1]))
        
    plt.grid(True)
    plt.axis('scaled')
    
    for iterate in iterates[0:n+1]:
        draw_polygon(iterate)
    
    plt.grid(True)
    plt.axis('scaled')
   
    
    plt.show()

# <markdowncell>

# The first iterate:

# <codecell>

draw_iterates(1)

# <markdowncell>

# We can add the second iterate to the mix:

# <codecell>

draw_iterates(2)

# <markdowncell>

# And why not add the next as well, just for fun:

# <codecell>

draw_iterates(3)

# <markdowncell>

# It's clear that the resulting parallelogram is stretching itself more and
# more along a line. This line is the *unstable manifold* of the
# origin. Since the map is *linear*, the unstable manifold is equal to the unstable *subspace* of the linearization (which
# is just the map itself, since it is linear).
# 
# The unstable subspace is given by the eigenvector whose eigenvalue is larger than $1$. Let's calculate these:

# <codecell>

from numpy import linalg

# <codecell>

lamb, v = linalg.eig(M)
lamb, v

# <markdowncell>

# Note that the eigenvectores are returned in the *columns* of the matrix. We can now add the eigenvector to our plot:

# <codecell>

fig, (ax1) = plt.subplots()

plt.plot([0, v[0,0]*8], [0, v[1,0]*8], 'k--', lw=0.5)
plt.arrow(0, 0, v[0,0]*6, v[1, 0]*6, axes=ax1, head_width=0.2, head_length=0.1, fc="g", ec="w", width=0.05)

draw_iterates(2)

# <codecell>

plt.plot([0, v[0,0]*15], [0, v[1,0]*15], 'k--', lw=0.5)
plt.arrow(0, 0, v[0,0]*20, v[1, 0]*20, axes=ax1, head_width=0.2, head_length=0.1, fc="g", ec="w", width=0.05)

draw_iterates(3)

# <headingcell level=3>

# Interpolating the Arnold cat map

# <markdowncell>

# To visualise the stretching action of the map in a more intuitive way, we could think about interpolating between the identity and the cat map. To look at that, we would like to do some symbolic computations, so we import the `sympy` package:

# <codecell>

import sympy

# <codecell>

from sympy import init_printing
init_printing()  # turn on pretty printing in the notebook

# <markdowncell>

# Let's define the identity matrix $\mathsf{I}$ and the cat map matrix $\mathsf{M}$:

# <codecell>

Identity = sympy.Matrix([[1, 0], [0, 1]])
MM = sympy.Matrix([[2, 1], [1, 1]])

Identity, MM

# <markdowncell>

# Let's try a linear interpolation with a parameter $\alpha$:

# <codecell>

alpha = sympy.symbols('alpha')
alpha

# <markdowncell>

# Let's define the linearly interpolated matrix $\mathsf{M}_\alpha := (1-\alpha) \mathsf{I} + \alpha \mathsf{M}$:

# <codecell>

M = lambda alpha: (1-alpha)*Identity + alpha*MM
M(alpha)

# <markdowncell>

# It's determinant is:

# <codecell>

det = M(alpha).det()
det

# <markdowncell>

# Let's linearly interpolate the  of the vertices, for example the furthest one, $(1, 1)$:

# <markdowncell>

# $$\mathbf{z}_\alpha = 
# \mathsf{M}_\alpha \left[\begin{pmatrix} 1 \\ 1 \end{pmatrix} \right]:$$

# <codecell>

z = lambda alpha: M(alpha) * sympy.Matrix([1,1])
z(alpha)

# <markdowncell>

# and now do the same with the other two vertices:

# <codecell>

x = lambda alpha: M(alpha) * sympy.Matrix([1,0])
y = lambda alpha: M(alpha) * sympy.Matrix([0,1])

origin = sympy.Matrix([0, 0])

vertices = lambda alpha: (origin, x(alpha), z(alpha), y(alpha))

[vertices(0), vertices(1)]
                          
                          

# <markdowncell>

# Let's calculate the area of the resulting parallelogram; note that the shape is *not*  a parallelogram, but rather an arbitrary quadrilateral. This is given in terms of the vectors describing the diagonals (lines joining opposite vertices) of the qualidrateral, $\mathbf{d}_1$ and $\mathbf{d}_2$, by
# 
# $$A = \frac{1}{2} \left| \mathbf{d}_1 \times \mathbf{d}_2 \right|; $$
# see [here (Wikipedia)](http://en.wikipedia.org/wiki/Quadrilateral#Vector_formulas).

# <codecell>

diag1 = lambda alpha: z(alpha) - origin
diag2 = lambda alpha: y(alpha) - x(alpha)

diag1(alpha), diag2(alpha)

# <codecell>

def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

# <codecell>

A = lambda alpha: cross(diag1(alpha), diag2(alpha)) / 2
A(alpha)

# <codecell>

sympy.simplify(_)

# <markdowncell>

# We wish this to be $1$ to have an area-preserving (*nonlinear*!) map, so we solve for $\beta$ to satisfy
# this constraint:

# <codecell>

sympy.solve(A(alpha)-1, alpha)

# <markdowncell>

# Thus this does *not* give an area-preserving map

# <markdowncell>

# So the new interpolating *nonlinear* map would be as follows:

# <markdowncell>

# We now have the coordinates of the 4 vertices of the new quadrilateral, given by $(0,0)$, $\mathbf{y}(\beta)$, $\mathbf{z}(\beta)$ and $\mathbf{x}(\alpha)$.

# <codecell>

y(beta).subs({alpha:0.5})

# <codecell>

origin = sympy.Matrix([0, 0])
origin

# <codecell>

new_vertices = lambda alpha, beta: [origin, y(beta), x(alpha), z(beta)]

# <codecell>

new_vertices_float = np.array([vertex.subs({alpha:0.5}).evalf() for vertex in new_vertices(alpha, beta)]) 
new_vertices_float

# <headingcell level=3>

# Correct attempt

# <markdowncell>

# Rather, we must recognise that if we stretch out the farthest corner, the other corners must be pulled *in*
# towards the diagonal $y=x$ in order to maintain the area-preserving property. To obtain a parallelogram, we must have a certain symmetry, as follows.

# <markdowncell>

# Let $\mathbf{z}_\alpha$ be obtained by linearly interpolating between the top right corner of the original square and that of the first iterate: 

# <codecell>

sympy.Lambda?

# <codecell>

interp_cat = sympy.Lambda((alpha, x), (1-alpha) * x + \
                          alpha * CatMap * x)

# <codecell>

z = sympy.Lambda(alpha, (1-alpha) * sympy.Matrix([1,1]) + \
alpha * CatMap * sympy.Matrix([1,1]))

z(alpha)

# <codecell>

print z(0), z(1)

# <codecell>

y = sympy.Lambda(alpha, (1-alpha) * sympy.Matrix([0,1]) + \
alpha * CatMap * sympy.Matrix([0,1]))

y(alpha)

# <codecell>

x = sympy.Lambda(alpha, (1-alpha) * sympy.Matrix([0,1]) + \
alpha * CatMap * sympy.Matrix([1,1]))

z(alpha)

# <markdowncell>

# To specify a parallelogram, we must now specify a vector $\mathbf{v}$ leaving from $\mathbf{z}_\alpha$ (or, equivalently, from the origin); specifying one of these
# two vectors specifies the other *uniquely* by the requirement (constraint) of being a parallelogram (opposite sides are equal vectors). The set of such vectors is two-dimensional.
# 
# If we now impose the requirement (constraint) that the area of the parallelogram is equal to $1$, then we should have a manifold of *dimension $1$* as the possible set of vectors $\mathbf{v}$. In other words, we have the freedom to choose one parameter of the vector $\mathbf{v}$ -- say, either the angle or the length of the vector.

# <markdowncell>

# One reaosonable choice is for the point $\mathbf{y}_\alpha$, the top left corner, to itself linearly interpolate between *its* own starting and finishing points.

# <codecell>

from sympy import Symbol
from sympy import Lambda
x= Symbol('x')
f = Lambda(x, x**2)
f

# <codecell>

unit_square

# <codecell>

expand_contract = lambda factor: sympy.Matrix([[factor, 0], [0, 1./factor]])
expand_contract(np.sqrt(5))

# <codecell>

M1 = np.array(expand_contract(np.sqrt(5))).astype(float)

# <codecell>

R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# <codecell>

shear = lambda d: np.array([[1, d], [0, 1]])

# <codecell>

np.ar

# <codecell>

np.arctan2?

# <codecell>

transf = np.dot(M1, shear(1./np.sqrt(5.)))
#transf = np.dot(shear(0.5), transf)
transf = np.dot(R(np.arctan2(1., 2.)), transf)

# <codecell>

draw_polygon(unit_square)
draw_polygon(map_poly(lambda x: np.dot(transf,x), unit_square))
plt.axis('scaled')

# <codecell>

sympy.cos(sympy.atan(

# <codecell>

sympy.atan(sympy.Rational(1,2))

# <codecell>

sympy.cos(_)

# <headingcell level=1>

# The real Arnold cat map

# <codecell>

new_square_vertices = [vertex + np.array([10., 0.]) for vertex in unit_square.vertices]
new_square = DirectedPolygon(new_square_vertices)
find_starting_point(unit_square, new_square)

