# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%matplotlib inline
%load_ext retina

# <codecell>

import matplotlib as mpl
import numpy as np

from matplotlib import pyplot as plt

# <codecell>

x = np.arange(-5, 5, 0.01)
y = x*x

plt.plot(x, y)
plt.show()

