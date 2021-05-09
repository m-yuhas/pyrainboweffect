# Pychedelic
[中文指南](https://github.com/m-yuhas/pychedelic/blob/main/doc/读我档案.md)

[Documentación en español](https://github.com/m-yuhas/pychedelic/blob/main/doc/LÉAME.md)

[Documentation en français](https://github.com/m-yuhas/pychedelic/blob/main/doc/LISEZ-MOI.md)

## Introduction
Take an image like this:
![image](https://github.com/m-yuhas/pychedelic/blob/main/images/demo0_in.png)

And transform it to this:
![image](https://github.com/m-yuhas/pychedelic/blob/main/images/demo0_out.gif)

## Quick Start
* Install the package:

```
pip install pychedelic
```

### Python API
In a Python console, import the package:

```python
>>> import pychedelic
```

Apply the effect to an image file and save the result as a gif:

```python
>>> pychedelic.psychedelic_gif('input.png', 'output.gif')
```

Apply the effect to an image file and save the result as an mp4:

```python
>>> pychedelic.psychedelic_mp4('input.png', 'output.gif')
```

### CLI
To use the CLI:

```bash
$ python -m pychedelic input.png output.gif
```

## API Documentation
For the complete API documentation, [click here](https://github.com/m-yuhas/pychedelic/blob/main/doc/api_documentation.md).

## Theory of Operation
It looks like this effect can be generated with the following steps:
1. Convert the image to greyscale
2. Partition the intensity space into the same number of partitions as colors
  in the color scheme.
3. Set the intesity regions to their corresponding colors
4. Increase the intensity of all pixels in the images (restarting at 0
  intensity if overflow occurs).
5. Go to step 2 and repeat until there are enough sequential frames to make an
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
- TODO: Apply the psychedelic effect to an animated image or video.
