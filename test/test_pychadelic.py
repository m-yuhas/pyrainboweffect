"""Unit test cases for the pychadelic module."""


import unittest


import numpy as np
import opencv
import pychadelic


class TestRainbowify(unittest.TestCase):
    """Test case for the rainbowify function."""

    def setUp(self) -> None:
        """Create some dummy data for the tests."""
        self.dummy_data = np.zeros((320, 240, 3), dtype=np.uint8)

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        output = pychadelic.rainbowify(self.dummy_data, 256)
        self.assertEqual(
            output.shape,
            (256, 320, 240, 3),
            'Output array is shaped improperly.')

    def test_custom_size(self) -> None:
        """Test function with custom output size."""
        output = pychadelic.rainbowify(self.dummy_data, 10, (10, 10))
        self.assertEqual(
            output.shape,
            (10, 10, 10, 3),
            'Output array is shaped improperly.')


class TestPsychadelicGif(unittest.TestCase):
    """Test case for psychadelic_gif function."""

    def setUp(self) -> None:
        """Create a dummy picture as input data for tests."""
        cv2.imwrite('temp.png', np.zeros(320, 240, 3), dtype=np.uint8)

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        pychadelic.psychadelic_gif('temp.png', 'output.gif')
        self.assertTrue(os.path.isfile('output.gif'), 'File not created')


class TestPsychadelicMp4(unittest.TestCase):
    """Test case for psychadelic_mp4 function."""

    def setUp(self) -> None:
        """Create a dummy picture as input data for tests."""
        cv2.imwrite('temp.png', np.zeros(320, 240, 3), dtype=np.uint8)

    def test_defaults(self) -> None:
        """Test function with default arguments."""
        pychadelic.psychadelic_mp4('temp.png', 'output.mp4')
        self.assertTrue(os.path.isfile('output.mp4'), 'File not created')


if __name__ == '__main__':
    unittest.main()
