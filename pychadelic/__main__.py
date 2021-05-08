"""CLI tools for pychadelic."""


import argparse


from .pychadelic import psychadelic_gif, psychadelic_mp4


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Add psychadelic effect to image.')
    parser.add_argument('input_file', help='Path to the input image file.')
    parser.add_argument('output_file', help='Output file path.')
    parser.add_argument(
        '-s',
        '--speed',
        type=float,
        default=60.0,
        help='FPS of the output.')
    parser.add_argument(
        '-d',
        '--duration',
        type=float,
        default=10.0,
        help='Output duration in seconds.')
    args = parser.parse_args()
    if args.output_file.endswith('.gif'):
        psychadelic_gif(
            args.input_file,
            args.output_file,
            output_size=None,
            speed=args.speed,
            duration=args.duration)
    elif args.output_file.endswith('.mp4'):
        psychadelic_mp4(
            args.input_file,
            args.output_file,
            output_size=None,
            speed=args.speed,
            duration=args.duration)
    else:
        print('Sorry, only *.mp4 and *.gif output files are supported.')
