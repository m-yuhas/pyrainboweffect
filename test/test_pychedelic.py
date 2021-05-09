"""Unit test cases for the pychedelic module."""


import os
import unittest


import cv2
import numpy as np
import pyrainboweffect


class TestRainbowify(unittest.TestCase):
    """Test case for the rainbowify function."""

    def setUp(self) -> None:
        """Create some dummy data for the tests."""
        self.dummy_data = np.zeros((320, 240, 3), dtype=np.uint8)

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        output = pyrainboweffect.rainbowify(self.dummy_data, 256)
        self.assertEqual(
            output.shape,
            (256, 320, 240, 3),
            'Output array is shaped improperly.')

    def test_custom_size(self) -> None:
        """Test function with custom output size."""
        output = pyrainboweffect.rainbowify(self.dummy_data, 10, (10, 10))
        self.assertEqual(
            output.shape,
            (10, 10, 10, 3),
            'Output array is shaped improperly.')


class TestPsychedelicGif(unittest.TestCase):
    """Test case for psychedelic_gif function."""

    def setUp(self) -> None:
        """Create a dummy picture as input data for tests."""
        cv2.imwrite('temp.png', np.zeros((320, 240, 3), dtype=np.uint8))

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        pyrainboweffect.psychedelic_gif('temp.png', 'output.gif')
        self.assertTrue(os.path.isfile('output.gif'), 'File not created')

    def tearDown(self) -> None:
        """Clean up any created files."""
        for file in os.listdir():
            if file.endswith('.png') or file.endswith('.gif'):
                try:
                    os.remove(file)
                except OSError:
                    pass


class TestPsychedelicMp4(unittest.TestCase):
    """Test case for psychedelic_mp4 function."""

    def setUp(self) -> None:
        """Create a dummy picture as input data for tests."""
        cv2.imwrite('temp.png', np.zeros((320, 240, 3), dtype=np.uint8))

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        pyrainboweffect.psychedelic_mp4('temp.png', 'output.mp4')
        self.assertTrue(os.path.isfile('output.mp4'), 'File not created')

    def tearDown(self) -> None:
        """Clean up any created files."""
        for file in os.listdir():
            if file.endswith('.png') or file.endswith('.mp4'):
                try:
                    os.remove(file)
                except OSError:
                    pass


if __name__ == '__main__':
    unittest.main()
