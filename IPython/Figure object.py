# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import base64
from IPython.core.pylabtools import print_figure

# <codecell>

class Figure(object):
    
    def __init__(self, figure, caption, label):
        self.figure = figure
        self.caption = caption
        self.label = label
        
    def _repr_html_(self):
        lines = ['<div class="myfigure">']
        #get figure as PNG:
        pngdata = print_figure(self.figure, 'png')
        b64png = base64.b64encode(pngdata)
        lines.append('<img src=data:png;base64,%s>' % b64png)
        
        lines.append("<p>%s</p>" % self.caption)
        lines.append("<b>%s</b>" % self.name)
        lines.append("</div>")
        
        return "\n".join(lines)
        
    

# <codecell>

%matplotlib inline

# <codecell>


# <headingcell level=1>


# <codecell>

from matplotlib import pyplot as plt
import numpy as np

# <codecell>

x = np.arange(-5, 5, 0.01)
y = x*x

# <codecell>

p = plt.plot(x, y)
plt.show()
f = plt.gcf()
png_data = print_figure(f, 'png')

# <codecell>

png_data

# <codecell>

from IPython.display import displayd

# <codecell>

display(p)

# <codecell>

f = Figure(png_data, "Hello", "name")

# <codecell>



# <codecell>

f._repr_html_()

# <codecell>


