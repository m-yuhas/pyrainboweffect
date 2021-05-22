
# pyrainboweffect
This module contains tools to apply the animated rainbow effect to images.

__CLI__

In addition to providing a Python API to add effects to images, this module
also provides a CLI tool.  This can be run from any terminal as follows:
```
python -m pyrainboweffect input.png ouput.mp4
```

__Module Level Constants__

When adding a psychedelic animation effect to an image, it is convinient to
choose the color scheme: the set of colors that appear in the output animation.
Three color schemes are provided by default as module level constants:
`SIX_COLOR_RAINBOW` is composed of red, yellow, cyan, blue, green, and magenta.
`PARTY_PARROT_RAINBOW` is based off the color palette used by the party parrot
gif.  The `PATRIOTIC_RAINBOW` color scheme consists only of red, white, and
blue.


# rainbowify
```python
rainbowify(
    image: 'np.array',
    n_frames: int,
    output_size: typing.Union[typing.Tuple[int], float] = None,
    color_scheme:
    typing.List[typing.Union[str, typing.Tuple[int]]] = ((255, 107, 107), (255, 107, 181), (255, 129, 255), (208, 129, 255), (129, 172, 255), (129, 255, 255), (129, 255, 129), (255, 208, 129), (255, 129, 129))
)
```
Rainbowify a single image and return the output as a numpy array.  The
rainbowification process is performed by converting the image to grayscale
and then assigning different colors to pixels within a certain brightness
range.  In the original image, each pixel's brightness is increased for
each output frame to create the motion effect.

__Args:__

- *image*: numpy array containing the original image.
- *n_frames*: number of successive frames to output.
- *output_size*: tuple in the form of (width, height); if this is set to
    None, then the original image size is used.  If output_size is a float,
    it is considered as a scale factor for the original image.
- *color_scheme*: list of colors to use in the output image sequence;
    colors can be in the form (B, G, R) where B, G, and R are integers
    or strings in the [`RRGGBB`](#RRGGBB) format.

__Returns:__

A numpy arrays containing the frames of the animated effect in the form
[frame, width, height, color channel]


# psychedelic_gif
```python
psychedelic_gif(
  input_file: str,
  output_file: str,
  output_size: typing.Union[typing.Tuple[int], float] = None,
  speed: float = 60.0,
  duration: float = 10.0,
  color_scheme:
    typing.List[typing.Union[str, typing.Tuple[int]]] = ((255, 107, 107), (255, 107, 181), (255, 129, 255), (208, 129, 255), (129, 172, 255), (129, 255, 255), (129, 255, 129), (255, 208, 129), (255, 129, 129)),
  meme_text: str = '')
```
Create a psychedelic gif givent the path to an input image file.

__Args:__

- *input_file*: path to input image file.
- *output_file*: path to output file.
- *output_size*: tuple in the form of (width, height) of the desired size.
    of the output gif; if set to None, then the size of the input image
    is used. If output_size is a float, it is considered as a scale factor
    for the original image.
- *speed*: fps of the output gif.
- *duration*: length of the ouptut gif in seconds.
- *color_scheme*: the palette of colors to use for the psychedeilic effect.
- *meme_text*: meme text to write across the top of animated gif.


# psychedelic_mp4
```python
psychedelic_mp4(
  input_file: str,
  output_file: str,
  output_size: typing.Union[typing.Tuple[int], float] = None,
  speed: float = 60.0,
  duration: float = 10.0,
  color_scheme:
    typing.List[typing.Union[str, typing.Tuple[int]]] = ((255, 107, 107), (255, 107, 181), (255, 129, 255), (208, 129, 255), (129, 172, 255), (129, 255, 255), (129, 255, 129), (255, 208, 129), (255, 129, 129)),
  meme_text: str = '')
```
Create a psychedelic mp4 givent the path to an input image file.

__Args:__

- *input_file*: path to input image file.
- *output_file*: path to output file.
- *output_size*: tuple in the form of (width, height) of the desired size.
    of the output gif; if set to None, then the size of the input image
    is used. If output_size is a float, it is considered as a scale factor
    for the original image.
- *speed*: fps of the output gif.
- *duration*: length of the ouptut gif in seconds.
- *color_scheme*: the palette of colors to use for the psychedelic effect.
- *meme_text*: meme text to write across the top of the video.

