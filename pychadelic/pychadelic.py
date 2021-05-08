"""Collection of functions to apply effects to images."""

from typing import List, Tuple, Union
import cv2
import moviepy.editor
import numpy as np


ColorScheme = List[Union[str, Tuple[int]]]


SIX_COLOR_RAINBOW = (
    (0xFF, 0x00, 0x00),
    (0xFF, 0xFF, 0x00),
    (0x00, 0xFF, 0x00),
    (0x00, 0xFF, 0xFF),
    (0x00, 0x00, 0xFF),
    (0xFF, 0x00, 0xFF))
PARTY_PARROT_RAINBOW = (
    (0xFF, 0x6B, 0x6B),
    (0xFF, 0x6B, 0xB5),
    (0xFF, 0x81, 0xFF),
    (0xD0, 0x81, 0xFF),
    (0x81, 0xAC, 0xFF),
    (0x81, 0xFF, 0xFF),
    (0x81, 0xFF, 0x81),
    (0xFF, 0xD0, 0x81),
    (0xFF, 0x81, 0x81))
PATRIOTIC_RAINBOW = (
    (0x00, 0x00, 0xFF),
    (0xFF, 0xFF, 0xFF),
    (0xFF, 0x00, 0x00))


def rainbowify(image: 'np.array',
               n_frames: int,
               output_size: Tuple[int] = None,
               color_scheme: ColorScheme = PARTY_PARROT_RAINBOW) -> 'np.array':
    """Rainbowify a single image and return the output as a numpy array.  The
    rainbowification process is performed by converting the image to grayscale
    and then assigning different colors to pixels within a certain brightness
    range.  In the original image, each pixel's brightness is increased for
    each output frame to create the motion effect.

    # Args:
    - *image*: numpy array containing the original image.
    - *n_frames*: number of successive frames to output.
    - *output_size*: tuple in the form of (width, height); if this is set to
        None, then the original image size is used.
    - *color_scheme*: list of colors to use in the output image sequence;
        colors can be in the form (B, G, R) where B, G, and R are integers
        or strings in the #RRGGBB format.

    # Returns:
    A list of numpy arrays containing the frames of the animated effect.
    """
    if output_size is None:
        output_size = (image.shape[1], image.shape[0])
    image = cv2.resize(image, output_size)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sequence = np.zeros((n_frames, image.shape[0], image.shape[1], 3))
    lbounds = [np.floor(x * 255 / len(color_scheme))
               for x in range(len(color_scheme))]
    ubounds = [np.floor((x+1) * 255 / len(color_scheme))
               for x in range(len(color_scheme))]
    bounds = zip(color_scheme, lbounds, ubounds)
    for idx in range(n_frames):
        for color, lower, upper in bounds:
            blue = np.where((image > lower) & (image <= upper), color[0], 0)
            green = np.where((image > lower) & (image <= upper), color[1], 0)
            red = np.where((image > lower) & (image <= upper), color[2], 0)
            # print(f"BLUE: {blue.shape}")
            # print(f"SEQUENCE: {sequence.shape}")
            sequence[idx, :, :, 0] += blue
            sequence[idx, :, :, 1] += green
            sequence[idx, :, :, 2] += red
        image += 1
    return np.uint8(sequence)


# pylint: disable=R0913
def psychadelic_gif(input_file: str,
                    output_file: str,
                    output_size: Tuple[int] = None,
                    speed: float = 60.0,
                    duration: float = 10.0,
                    color_scheme: ColorScheme = PARTY_PARROT_RAINBOW) -> None:
    """Create a psychadelic gif givent the path to an input image file.

    # Args:
    - *input_file*: path to input image file.
    - *output_file*: path to output file.
    - *output_size*: tuple in the form of (width, height) of the desired size.
        of the output gif; if set to None, then the size of the input image
        is used.
    - *speed*: fps of the output gif.
    - *duration*: length of the ouptut gif in seconds.
    - *color_scheme*: the palette of colors to use for the psychadeilic effect.
    """
    sequence = rainbowify(
        image=cv2.imread(input_file),
        n_frames=int(speed * duration),
        output_size=output_size,
        color_scheme=color_scheme)

    def make_frame(time):
        return sequence[int(time * speed), :, :, :]

    clip = moviepy.editor.VideoClip(make_frame, duration=duration)
    clip.write_gif(output_file, fps=speed)


# pylint: disable=R0913
def psychadelic_mp4(input_file: str,
                    output_file: str,
                    output_size: Tuple[int] = None,
                    speed: float = 60.0,
                    duration: float = 10.0,
                    color_scheme: ColorScheme = PARTY_PARROT_RAINBOW) -> None:
    """Create a psychadelic mp4 givent the path to an input image file.

    # Args:
    - *input_file*: path to input image file.
    - *output_file*: path to output file.
    - *output_size*: tuple in the form of (width, height) of the desired size.
        of the output gif; if set to None, then the size of the input image
        is used.
    - *speed*: fps of the output gif.
    - *duration*: length of the ouptut gif in seconds.
    - *color_scheme*: the palette of colors to use for the psychadeilic effect.
    """
    sequence = rainbowify(
        image=cv2.imread(input_file),
        n_frames=int(speed * duration),
        output_size=output_size,
        color_scheme=color_scheme)
    writer = cv2.VideoWriter(
        output_file,
        cv2.VideoWriter_fourcc(*'XVID'),
        speed,
        (sequence.shape[2], sequence.shape[1]))
    for i in range(sequence.shape[0]):
        writer.write(sequence[i, :, :, :])
    writer.release()
