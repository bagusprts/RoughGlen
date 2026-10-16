# test_roughglen.py
"""
Tests for RoughGlen module.
"""

import unittest
from roughglen import RoughGlen

class TestRoughGlen(unittest.TestCase):
    """Test cases for RoughGlen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughGlen()
        self.assertIsInstance(instance, RoughGlen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughGlen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
