"""
--------------------
many annotate_bubble
--------------------

"""

import mpl_visual_context.patheffects as pe
from mpl_speech_bubble import AnnotationBubble

if True:
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(num=1, clear=True, figsize=(7, 3))

    xy = (0.5, 0.5)
    ax.plot(xy[0], xy[1], "ro")

    for t in ["up", "down"]:
        ann = AnnotationBubble(t, xy, loc=t, dist=1., rotation=0, size=20)
        ax.add_artist(ann)

    xy = (1., 0.5)
    ax.plot(xy[0], xy[1], "go")

    for t in ["left", "right"]:
        ann = AnnotationBubble(t, xy, loc=t, dist=1.2, rotation=45, size=20,
                               arrowstyle="simple")
        ax.add_artist(ann)

    xy = (1.5, 0.5)
    ax.plot(xy[0], xy[1], "bo")

    for t, ha, dx in [("up", "left", -0.3), ("down", "right", 0.3)]:
        ann = AnnotationBubble(t, xy, loc=t, dist=1.2, rotation=0, size=20,
                               arrowstyle="fancy", ha=ha, dx=dx,
                               bbox=dict(boxstyle="square, pad=0.2",
                                         fc="none", ec="k")
                               )
        ax.add_artist(ann)

    xy = (2., 0.5)
    ax.plot(xy[0], xy[1], "yo")

    arrowprops = dict(arrowstyle="wedge, tail_width=1, shrink_factor=0.5",
                      connectionstyle="arc3",
                      patchA=None, shrinkB=5)
    bbox_circle = dict(boxstyle="fixed_circle, pad=0.2",
                       fc="none", ec="k")
    bbox_square = dict(boxstyle="fixed_square, pad=0.1",
                       fc="none", ec="k")

    for t, c, bbox in zip(["up", "down", "left", "right"],
                          "abcd",
                          [bbox_circle, bbox_circle, bbox_square, bbox_square]):
        ann = AnnotationBubble(c, xy, loc=t, dist=1.3, rotation=20, size=20,
                               ha="center", va="center",
                               bbox=bbox, arrowprops=arrowprops
                               )
        ann.get_bbox_patch().set_path_effects([pe.Glow(alpha_line=0.1),
                                               pe.FillColor("w")])
        ax.add_artist(ann)

    ax.set(xlim=(0.2, 2.3), ylim=(0.4725, 0.5275))
    plt.show()
