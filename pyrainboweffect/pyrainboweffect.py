"""Collection of functions to apply effects to images."""

from typing import List, Tuple, Union
import cv2
import numpy as np
from PIL import Image


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
MEME_TEXT_HEIGHT = 0.15
MEME_TEXT_WIDTH = 0.9


def rainbowify(image: 'np.array',
               n_frames: int,
               output_size: Union[Tuple[int], float] = None,
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
        None, then the original image size is used.  If output_size is a float,
        it is considered as a scale factor for the original image.
    - *color_scheme*: list of colors to use in the output image sequence;
        colors can be in the form (B, G, R) where B, G, and R are integers
        or strings in the #RRGGBB format.

    # Returns:
    A numpy arrays containing the frames of the animated effect in the form
    [frame, width, height, color channel]
    """
    if output_size is None:
        output_size = (image.shape[1], image.shape[0])
    elif isinstance(output_size, float):
        output_size = (int(image.shape[1] * output_size),
                       int(image.shape[0] * output_size))
    image = cv2.resize(image, output_size)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sequence = np.zeros((n_frames, image.shape[0], image.shape[1], 3))
    lbounds = [np.floor(x * 256 / len(color_scheme))
               for x in range(len(color_scheme))]
    ubounds = [np.floor((x+1) * 256 / len(color_scheme))
               for x in range(len(color_scheme))]
    bounds = list(zip(color_scheme, lbounds, ubounds))
    for idx in range(n_frames):
        for color, lower, upper in bounds:
            blue = np.where((image >= lower) & (image < upper), color[0], 0)
            green = np.where((image >= lower) & (image < upper), color[1], 0)
            red = np.where((image >= lower) & (image < upper), color[2], 0)
            sequence[idx, :, :, 0] += blue
            sequence[idx, :, :, 1] += green
            sequence[idx, :, :, 2] += red
        image += 1
    return np.uint8(sequence)


def add_meme_text(image_sequence: 'np.array', text: str) -> 'np.array':
    """Add meme text to an animated sequence of images.

    # Args:
    - *image_sequence*: numpy array in the form
        [frame, width, height, color channel]
    - *text*: the text to add to every frame in the sequence.  Text will be
        white in color and take up `MEME_TEXT_HEIGHT` percentage of image
        height and `MEME_TEXT_WIDTH` percentage of image width.  The text will
        be centered horizontally and appear `MEME_TEXT_HEIGHT / 2` percent from
        the top of each frame.

    # Returns:
    A numpy arrays containing the frames with added text in the form
    [frame, width, height, color channel]
    """
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 1)
    text_image = np.zeros((text_size[1] * 2, text_size[0], 3), dtype=np.uint8)
    text_image = cv2.putText(
        text_image,
        text,
        (0, text_size[1]),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        fontScale=1,
        color=(255, 255, 255),
        thickness=1)
    text_image = cv2.resize(
        text_image,
        (
            int(image_sequence.shape[2] * MEME_TEXT_WIDTH),
            int(image_sequence.shape[1] * MEME_TEXT_HEIGHT)))
    text_image = np.repeat(
        text_image[np.newaxis, :, :, :],
        image_sequence.shape[0],
        axis=0)
    x_start = int(MEME_TEXT_HEIGHT * image_sequence.shape[1] / 2)
    y_start = int((1 - MEME_TEXT_WIDTH) * image_sequence.shape[2] / 2)
    x_end = x_start + text_image.shape[1]
    y_end = y_start + text_image.shape[2]
    image_sequence[:, x_start:x_end, y_start:y_end, :] |= text_image
    return image_sequence


# pylint: disable=R0913
def psychedelic_gif(input_file: str,
                    output_file: str,
                    output_size: Union[Tuple[int], float] = None,
                    speed: float = 60.0,
                    duration: float = 10.0,
                    color_scheme: ColorScheme = PARTY_PARROT_RAINBOW,
                    meme_text: str = '') -> None:
    """Create a psychedelic gif givent the path to an input image file.

    # Args:
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
    """
    sequence = rainbowify(
        image=cv2.imread(input_file),
        n_frames=int(speed * duration),
        output_size=output_size,
        color_scheme=color_scheme)
    if meme_text != '':
        sequence = add_meme_text(sequence, meme_text)
    pil_images = []
    for i in range(sequence.shape[0]):
        cv_image = cv2.cvtColor(sequence[i, :, :, :], cv2.COLOR_BGR2RGB)
        pil_images.append(Image.fromarray(cv_image))
    pil_images[0].save(
        output_file,
        save_all=True,
        append_images=pil_images[1:],
        duration=int(1000 / speed),
        loop=0)


# pylint: disable=R0913
def psychedelic_mp4(input_file: str,
                    output_file: str,
                    output_size: Union[Tuple[int], float] = None,
                    speed: float = 60.0,
                    duration: float = 10.0,
                    color_scheme: ColorScheme = PARTY_PARROT_RAINBOW,
                    meme_text: str = '') -> None:
    """Create a psychedelic mp4 givent the path to an input image file.

    # Args:
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
    """
    sequence = rainbowify(
        image=cv2.imread(input_file),
        n_frames=int(speed * duration),
        output_size=output_size,
        color_scheme=color_scheme)
    if meme_text != '':
        sequence = add_meme_text(sequence, meme_text)
    writer = cv2.VideoWriter(
        output_file,
        cv2.VideoWriter_fourcc(*'XVID'),
        speed,
        (sequence.shape[2], sequence.shape[1]))
    for i in range(sequence.shape[0]):
        writer.write(sequence[i, :, :, :])
    writer.release()
