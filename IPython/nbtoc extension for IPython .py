# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# The IPython `nbtoc` extension uses a (relatively) small piece of javascript to implement a poppable table of contents view of the notebook
# structure. To use it, do the following steps using IPython magic commands:

# <codecell>

%install_ext https://raw.github.com/minrk/ipython_extensions/master/nbtoc.py

# <codecell>

%load_ext nbtoc

# <markdowncell>

# Now running the `%nbtoc` IPython magic pops up the table of contents. This maps *only* the heading cells in the notebook, *not* 
# "headings" inside Markdown cells notated with `###` etc. The table of contents currently does *not* update automatically; `%nbtoc` must be 
# rerun to upate the contents list.

# <codecell>

%nbtoc

# <codecell>

%install_ext??

# <headingcell level=1>

# Example section

# <headingcell level=1>

# Another section

# <headingcell level=2>

# A subsection

# <headingcell level=3>

# A level 3 heading

# <headingcell level=2>

# Another subsection

# <headingcell level=1>

# Last section

# <codecell>


