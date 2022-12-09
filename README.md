# mpl-speech-bubble

A proof-of-concept package to draw speech bubble. It is basically MPL's
annotation and it merges the arrow patch and bbox patch using [skia-pathops](https://github.com/fonttools/skia-pathops). The
package is far from complete and only recommended for an advanced MPL user who
are well familiar with how annotation works.

<img src="https://user-images.githubusercontent.com/95962/206708676-6e3cada0-9d37-447b-82cf-4c1c20425b9b.png">

```python
from mpl_speech_bubble import annotate_bubble

ann = annotate_bubble(ax, 'speech\nbubble',
                      xy=(4, 4), xycoords='data',
                      xytext=(-10, -25), textcoords='offset points',
                      size=20, color="w",
                      ha="left", va="top",
                      bbox=dict(boxstyle="round",
                                fc="none", ec="w"),
                      arrowprops=dict(arrowstyle="wedge,tail_width=2.",
                                      patchA=None,
                                      patchB=el,
                                      relpos=(0.5, 0.5),
                                      connectionstyle="arc3,rad=-0.1"))
```

Check out `examples/example.py` for full example.

## Installation

The package is not available at pip. You can clone the git repository and
install from the source.:

```bash
pip install .
```

## Development Installation


```bash
pip install -e ".[dev]"
```

