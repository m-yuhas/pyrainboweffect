# Pychadelic

## Introduction
Take an image like this:

And change it to this:

## Quick Start
* Install the package:

```
pip install pychadelic
```

### Python API
In a Python console, import the package:

```python
>>> import pychadelic
```

Apply the effect to an image file and save the result as a gif:

```python
>>> pychadelic.psychadelic_gif('input.png', 'output.gif')
```

Apply the effect to an image file and save the result as an mp4:

```python
>>> pychadelic.psychadelic_mp4('input.png', 'output.gif')
```

### CLI
To use the CLI:

```bash
$ python -m pychadelic input.png output.gif
```

## API Documentation
For the complete API documentation, [click here](https://github.com/m-yuhas/pychadelic/blob/master/doc/api_documentation.md).

## Theory of Operation
It looks like this effect can be generated with the following steps:
1. Convert the image to greyscale
2. Partition the intensity space into the same number of partitions as colors
  in the color scheme.
3. Set the intesity regions to their corresponding colors
4. Increase the intensity of all pixels in the images (restarting at 0
  intensity if overflow occurs).
5. Go to step 2 and repeat until there are enough sequential frams to make an
  animation.

## Dependencies
Only Python version 3.5 and greater are supported.  This package should run on
any POSIX system as well as Windows 7 and greater.

The following Pypi packages are required:
* moviepy
* numpy
* opencv-python

## Contributing
Suggestions and pull requests are welcome.  If you find a bug and don't have
time to fix it yourself, feel free to open an issue.

## Future Tasks
- TODO: Apply the psychadelic effect to an animated image or video.
