import logging
import numpy as np
import matplotlib.patches as mpatches

from matplotlib.text import Text, Annotation
import matplotlib.transforms as mtransforms

_log = logging.getLogger(__name__)

from .mpl_pathops import mpl2skia, skia2mpl, union


class AnnotationBubble(Annotation):
    def __init__(self, *kl, **kwargs):
        super().__init__(*kl, **kwargs)

        self._bbox_patch.set_visible(False)

    def _get_bbox_patch_path(self, renderer):

        # copied from Text.draw
        with self._cm_set(text=self._get_wrapped_text()):
            bbox, info, descent = self._get_layout(renderer)
            trans = self.get_transform()

            # don't use self.get_position here, which refers to text
            # position in Text:
            posx = float(self.convert_xunits(self._x))
            posy = float(self.convert_yunits(self._y))
            posx, posy = trans.transform((posx, posy))
            if not np.isfinite(posx) or not np.isfinite(posy):
                _log.warning("posx and posy should be finite values")
                return None, None

            # Update the location and size of the bbox
            # (`.patches.FancyBboxPatch`), and draw it.
            if self._bbox_patch:
                self.update_bbox_position_size(renderer)
                self._bbox_patch.draw(renderer)
                return (self._bbox_patch.get_path(),
                        self._bbox_patch.get_transform())
                        # self._bbox_patch.get_patch_transform())
            else:
                return None, None


    def draw(self, renderer):
        # docstring inherited
        if renderer is not None:
            self._renderer = renderer
        if not self.get_visible() or not self._check_xy(renderer):
            return
        # Update text positions before `Text.draw` would, so that the
        # FancyArrowPatch is correctly positioned.
        self.update_positions(renderer)
        self.update_bbox_position_size(renderer)
        if self.arrow_patch is not None:  # FancyArrowPatch
            if self.arrow_patch.figure is None and self.figure is not None:
                self.arrow_patch.figure = self.figure

            p1, t1 = self._get_bbox_patch_path(renderer)
            p2, t2 = (self.arrow_patch.get_path(),
                      self.arrow_patch.get_patch_transform())
            s1 = mpl2skia(p1, t1)
            s2 = mpl2skia(p2, t2)

            u = union(s1, s2)
            p12 = skia2mpl(u)

            patch = mpatches.PathPatch(p12, facecolor='w', ec="k")

            patch.update_from(self._bbox_patch)
            patch.set_visible(True)
            patch.set_transform(mtransforms.IdentityTransform())
            patch.draw(renderer)

        # Draw text, including FancyBboxPatch, after FancyArrowPatch.
        # Otherwise, a wedge arrowstyle can land partly on top of the Bbox.
        # self.text_draw(renderer)
        Text.draw(self, renderer)


def annotate_bubble(ax, text, xy, xytext=None, xycoords='data',
                    textcoords=None,
                    arrowprops=None, annotation_clip=None, **kwargs):
    # Signature must match Annotation. This is verified in
    # test_annotate_signature().
    a = AnnotationBubble(text, xy, xytext=xytext, xycoords=xycoords,
                         textcoords=textcoords, arrowprops=arrowprops,
                         annotation_clip=annotation_clip, **kwargs)
    a.set_transform(mtransforms.IdentityTransform())
    if 'clip_on' in kwargs:
        a.set_clip_path(ax.patch)
    ax._add_text(a)
    return a

