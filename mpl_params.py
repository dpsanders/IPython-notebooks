# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Interrogating matplotlib parameter settings in matplotlib.parameters

# <markdowncell>

# The styling of `matplotlib` plots is highly configurable via parameter settings stored in the data structure `matplotlib.mpl_params` inside `matplotlib` (formerly called `matplotlib.rcParams`).
# 
# `mpl_params` behaves similarly to a dictionary, i.e. it is a collection of key-value pairs, but it also has *validation*,
# meaning that the possible values associated to a given key may be restricted.
# 
# For a key `key`, querying `mpl_params[key]` returns the current value associated to the key `key`, while
# 
#     mpl_params[key] = value
#     
# associates the new value `value` to the key `key`.
# 

# <codecell>

%matplotlib

# <codecell>

import matplotlib as mpl
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import rcParams

mpl_params = rcParams

# <markdowncell>

# Since there are many configurable options in `mpl.parameters`,
# it is useful to restrict attention to a subset of interest.
# For example, we can list all of the keys containing the string `font` as follows:

# <codecell>

font_keys = [k for k in mpl_params.keys() if 'font' in k]
print font_keys

# <markdowncell>

# We could define a function for this:

# <codecell>

def get_keys_containing(word):
    ''' 
    Returns the `matplotlib.rcParams` keys which contain the string `word`.
    '''
    
    keys = [k for k in mpl_params.keys() if word in k]
    return keys

# <markdowncell>

# and use it like so:

# <codecell>

font_keys = get_keys_containing('font')
print font_keys

# <markdowncell>

# Now we define a function to make a string with key-value pairs:

# <codecell>

def format_key_value_pairs(word):
    
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

