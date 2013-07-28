# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

"""
Defines DirectedLineSegment and  DirectedPolygon classes
"""

# <codecell>

import numpy as np

# <codecell>

def norm(x):
	return np.sqrt(np.dot(x, x))

class DirectedLineSegment:
    """A directed line segment from `start` to `end`
    v is the *non-normalized* vector start - end
    It is non-normalized so that the segment is parametrized by start + t*v, 
    where t=0 gives start and t=1 gives end
    
    The normal vector n is normalized.
    """

    def __init__(self, start, end):
        self.start, self.end = np.asarray(start, dtype=float), np.asarray(end, dtype=float)
        self.v = self.start - self.end
        
        self.n = np.array([-self.v[1], self.v[0]])
        self.n /= norm(self.n)
        
    def __repr__(self):
        return "DirectedLineSegment" + self.__str__()
    def __str__(self):
        return "([%g, %g], [%g, %g])" % (self.start[0], self.start[1], self.end[0], self.end[1])

# <codecell>

def find_intersection_segments(segment1, segment2):
    """Find intersection of two line segments
    
    Returns the value of t corresponding to the parametrization of segment1 at the intersection point,
    or None if they do not intersect within the segment ends
    
    Use representation with normal of ls2 for simplicity
    
    Parametrize segment1  as  p1 + t.v
    Use representation of segment2 as {x:(x-c).n = 0}
    """
    
    n = segment2.n
    c = segment2.start
    
    x = segment1.start
    v = segment1.v
    
    
    threshold = 1.e-15
    
    if abs(np.dot(v,n)) < threshold:  # 0: lines are parallel
        return None
    
    
    t_star = np.dot(c - x, n) / np.dot(v, n)  # intersection time
    
    if 0.0 <= t_star <= 1.0:
        return (t_star, x + t_star * v)
    
    else:
        return None

# <codecell>

def test_find_intersection_segments():

    segment1 = DirectedLineSegment([0, 0], [1, 1])
    segment2 = DirectedLineSegment([0, 1], [1, 0])
    
    t_star, intersection_point = find_intersection_segments(segment1, segment2)
    assert t_star == 0.5
    assert all(intersection_point == np.array([0.5, 0.5]))
    
    
    # parallel lines:
    segment1 = DirectedLineSegment([0, 0], [1, 1])
    segment2 = DirectedLineSegment([3, 3], [4, 4])

    assert find_intersection_segments(segment1, segment2) == None
    
    
    segment1 = DirectedLineSegment([0, 0], [1, 1])
    segment2 = DirectedLineSegment([1, 1], [1, 2])
    
    t_star, intersection_point = find_intersection_segments(segment1, segment2)
    assert t_star == 1.0
    assert all(intersection_point == np.array([1.0, 1.0]))
    

# <headingcell level=3>

# Polygons

# <markdowncell>

# Next we join line segments up into directed polygons. Here we are assuming that the polygons are closed loops, i.e. that there is a link from the last vertex back to the first. 

# <codecell>

class DirectedPolygon:
    """A directed polygon
    
    Parameters
    ==========
    vertices:
        a list of vertices
    """
        
    
    def __init__(self, vertices):
        self.vertices = np.asarray(vertices)
        
        self.segments = []
        
        for i in range(len(self.vertices)-1):
            self.segments.append(DirectedLineSegment(self.vertices[i], vertices[i+1]))
            
        self.segments.append(DirectedLineSegment(vertices[-1], vertices[0]))

    def __repr__(self):
        return self.vertices.__repr__()
    
    def draw(self):
        plt.fill(self.vertices[:,0], self.vertices[:,1], alpha=0.5)
        

# <codecell>

def find_starting_point(polygon1, polygon2):
    """Find the starting point of the intersection of two polygons
    Returns None if they do not intersect"""
    
    for i in range(len(polygon1.segments)):
        for j in range(len(polygon2.segments)):
            
            segment1 = polygon1.segments[i]
            segment2 = polygon2.segments[i]
            
            intersection = find_intersection_segments(segment1, segment2)
            
            if intersection:
                return (intersection[1], i, j)  # don't need the intersection time
            
    return None
            
    

def intersection_polygons(polygon1, polygon2):
    """Calculate intersection of two (convex) polygons
    First find an intersection point.
    Then follow this around by taking consecutive pieces of each polygon?
    """
    
    starting_point, i, j = find_starting_point(polygon1, polygon2)
    # i is the number of the segment of the first polygon, j of the second
    
    if starting_point is None:
        return None
    
    intersection_path = [starting_point]
    
    current_segment = polygon2.segments[j]
    remainder = DirectedLineSegment(starting_point, current_segment.end)
    
#    find_intersection_segments(remainder 

# <codecell>

def test_find_starting_point():
    
    unit_square = DirectedPolygon([(0.,0.), (1.,0.), (1.,1.), (0.,1.)])
    
    theta = np.pi / 4.
    R = np.array([np.cos(theta), np.sin(theta), -np.sin(theta), np.cos(theta)]).reshape((2,2) )
    
    rotated_square_vertices = [np.dot(R, vertex) for vertex in unit_square.vertices]
    rotated_square = DirectedPolygon(rotated_square_vertices)
    
    
    starting_point = find_starting_point(unit_square, rotated_square)
    
    assert starting_point[0] == 0.0
    assert all(starting_point[1] == np.array([0.0, 0.0]))
    
    
    new_square = [vertex + np.array([10., 0.]) for vertex in unit_square.vertices]
    
    starting_point = find_starting_point(unit_square, new_square)
    
    assert starting_point == None

# <codecell>

class ParametrizedFunctionSegment:
    """Represents a 'segment' of a parametrized function
    
    f : [0,1] -> R^2
    """

    def __init__(self, f, interval=[0, 1]):
        self.f = f
        self.start = interval[0]
        self.end = interval[1]

# <codecell>

def intersection_function_segments(f1, f2):
    """ 
    Solve f1(s) = f2(t)
    Two nonlinear equations in two unknowns
    
    i.e.
    F(s, t) = 0
    
    where F(s,t) := f1(s) - f2(t)
    """
    
    F = lambda(s, t): f1(s) - f2(t)
    
    # Call Newton or something to find zeros of F!
    
    # Or just do it lazily: build up a complicated function e.g. in sympy, then solve at last possible moment
    
    # NB: IF want e.g. intersection of a parametrized curve with a known *straight* line, then this reduces to a *1D* root-finding problem.

# <codecell>

def map_parametrized_curve(Phi, f):
    """When apply a map Phi:R^2->R^2 to a parametrized curve f:[0,1] -> R^2, we get 
    the composition (Phi \circ f), the composition (Phi \circ f)(t) = Phi(f(t)) 
    """

    
    return ParametrizedFunctionSegment(lambda t: Phi(f(t)) )

