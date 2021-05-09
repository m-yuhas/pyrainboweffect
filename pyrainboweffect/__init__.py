"""This module contains tools to apply the animated rainbow effect to images.

# CLI
In addition to providing a Python API to add effects to images, this module
also provides a CLI tool.  This can be run from any terminal as follows:
```
python -m pychedelic input.png ouput.mp4
```

# Module Level Constants
When adding a psychedelic animation effect to an image, it is convinient to
choose the color scheme: the set of colors that appear in the output animation.
Three color schemes are provided by default as module level constants:
`SIX_COLOR_RAINBOW` is composed of red, yellow, cyan, blue, green, and magenta.
`PARTY_PARROT_RAINBOW` is based off the color palette used by the party parrot
gif.  The `PATRIOTIC_RAINBOW` color scheme consists only of red, white, and
blue.
"""


from .pyrainboweffect import *
