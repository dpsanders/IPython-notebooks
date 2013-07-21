# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Interrogating and modifying matplotlib parameter settings via matplotlib.mpl_params

# <markdowncell>

# The styling of `matplotlib` plots is highly configurable. In this mini-tutorial, we will see how *any* parameter that contributes to the look and design of a `matplotlib` plot may be changed at any time, with an *immediate* and *striking* influence on how the plot looks!

# <headingcell level=2>

# The `mpl_params` data structure for parameter settings

# <markdowncell>

#  The configuration is done via parameter settings stored in a data
# structure called `mpl_params`. This lives inside the `matplotlib` namespace, 
# so we can import it using:

# <codecell>

from matplotlib import rcParams
mpl_params = rcParams

# <markdowncell>

# In future versions of `matplotlib`, we will be able to use simply
# 
#     from matplotlib import mpl_params
#     
# but at the moment we must rather create the name `mpl_params` as an alias of the current name `rcParams` for the structure

# <markdowncell>

# `mpl_params` behaves like a dictionary, i.e. it is a collection of key-value pairs. But it also has *validation*,
# which means that the possible values associated to a given key may be restricted to a certain set.
# 
# For a key `key`, querying `mpl_params[key]` returns the current value associated to the key `key`, while
# 
#     mpl_params[key] = value
#     
# associates the new value `value` to the key `key`. For example:

# <codecell>

print mpl_params['font.size']

# <codecell>

mpl_params['font.size'] = 20
print mpl_params['font.size']

# <headingcell level=2>

# Example of styling a plot

# <markdowncell>

# To see what effect changing these values has on a `matplotlib` plot, let's make a simple plot twice, changing the font size in between. Firstly we initialize the plotting environment in the IPython notebook:

# <codecell>

%matplotlib inline

# <markdowncell>

# Now we import the parts of `matplotlib` and `numpy` that we will use:

# <codecell>

from matplotlib import pyplot as plt
import numpy as np

# <markdowncell>

# Since we will be repeating the same operation, instead of duplicating the code, it is cleaner to create a function to do the plotting:

# <codecell>

def simple_plot():
    x = np.arange(-5, 5, 0.01)
    y = x * x
    
    plt.plot(x,y)

# <markdowncell>

# Now we can do the plotting, firstly with the `matplotlib` defaults, and then with the new font size:

# <codecell>

simple_plot()  # with default values since we have not changed anything yet

# <codecell>

mpl_params['font.size'] = 20
simple_plot()  # rerun the plot, now with the new font size

# <markdowncell>

# Hey presto! The fonts are now much more readable for this small size of figure.

# <headingcell level=2>

# Great! What can I change?

# <markdowncell>

# *All* of the parameters of a plot are modifiable in this simple way. Here is a list (actually, a dictionary), of the entire contents of `mpl_params`. Note how the IPython notebook automatically creates a scrolling region when the output is too long.

# <codecell>

print mpl_params

# <markdowncell>

# That can be a bit unwieldy to manage! Suppose I want to know what I can change about `axes`. It's easy enough to find all of the keys which *begin*  with the word `axes`, but what about those containing the character string `axes` elsewhere? Here is a utility function to extract all of those keys containing a certain character string:

# <codecell>

def get_keys_containing(word):
    ''' 
    Returns those keys in `mpl_params` which contain the string `word`.
    '''
    
    keys = [k for k in mpl_params.keys() if word in k]
    return keys


def format_key_value_pairs(word):
    '''
    Returns a list, formatted as a string, of all key-value pairs in `mpl_params` whose keys contain the string `word`
    '''
    
    output = ""
    
    keys = get_keys_containing(word)
    
    for item in keys:
        key = "'{}'".format(item)
        value = mpl_params[item]
    
        pair = ("{:>40}:{}".format(key, value))
        
        output += pair + "\n"
    
    return output

# <codecell>

font_keys = format_key_value_pairs("font")
edge_keys = format_key_value_pairs("edge")

print font_keys, edge_keys

# <headingcell level=2>

# What's next?

# <markdowncell>

# That's all there is to it. Now just sit down and play around. Remember that since we are working in the IPython Notebook (where else?!), we can play around and tweak to our heart's content, running the same cell over and over again by executing the cell with `Ctrl-Enter`, instead of `Shift-Enter`.

# <markdowncell>

# Happy style hunting!

