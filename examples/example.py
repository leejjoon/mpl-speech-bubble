"""
---------------
annotate_bubble
---------------

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from mpl_speech_bubble import annotate_bubble

fig, ax = plt.subplots(num=1, clear=True)
arr = np.arange(100).reshape((10, 10))
ax.imshow(arr, interpolation="bilinear")

el = Ellipse((4, 4), 0.5, 0.5, color="y")
ax.add_patch(el)

ann = annotate_bubble(ax, 'speech\nbubble',
                      xy=(4, 4), xycoords='data',
                      loc="up",
                      size=20, color="w",
                      ha="left",
                      bbox=dict(boxstyle="round",
                                fc="none", ec="w"),
                      arrowprops=dict(arrowstyle="wedge,tail_width=1.5",
                                      patchA=None,
                                      patchB=el,
                                      connectionstyle="arc3,rad=-0.1"))

plt.show()
