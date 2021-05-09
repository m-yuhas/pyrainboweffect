"""Unit test cases for the pychedelic module."""


import os
import unittest


import cv2
import numpy as np
import pychedelic


class TestRainbowify(unittest.TestCase):
    """Test case for the rainbowify function."""

    def setUp(self) -> None:
        """Create some dummy data for the tests."""
        self.dummy_data = np.zeros((320, 240, 3), dtype=np.uint8)

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        output = pychedelic.rainbowify(self.dummy_data, 256)
        self.assertEqual(
            output.shape,
            (256, 320, 240, 3),
            'Output array is shaped improperly.')

    def test_custom_size(self) -> None:
        """Test function with custom output size."""
        output = pychedelic.rainbowify(self.dummy_data, 10, (10, 10))
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
        pychedelic.psychedelic_gif('temp.png', 'output.gif')
        self.assertTrue(os.path.isfile('output.gif'), 'File not created')


class TestPsychedelicMp4(unittest.TestCase):
    """Test case for psychedelic_mp4 function."""

    def setUp(self) -> None:
        """Create a dummy picture as input data for tests."""
        cv2.imwrite('temp.png', np.zeros((320, 240, 3), dtype=np.uint8))

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        pychedelic.psychedelic_mp4('temp.png', 'output.mp4')
        self.assertTrue(os.path.isfile('output.mp4'), 'File not created')


if __name__ == '__main__':
    unittest.main()
