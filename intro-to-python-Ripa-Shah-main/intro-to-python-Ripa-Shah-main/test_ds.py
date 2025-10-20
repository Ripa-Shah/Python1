"""
Unit tests for data science functions.

This module contains unit tests for the functions: compute_mean,
compute_median, compute_mode, and compute_range from the `assignment` module.
"""

import unittest
from ds import compute_mean, compute_median, compute_mode, compute_range


class TestDataScienceFunctions(unittest.TestCase):
    """Test suite for data science functions."""

    def test_compute_mean(self):
        """Test cases for the compute_mean function."""
        self.assertEqual(compute_mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(compute_mean([10, 20, 30, 40, 50]), 30)
        self.assertEqual(compute_mean([-1, 0, 1]), 0)
        self.assertIsNone(compute_mean([]))  # Empty list

    def test_compute_median(self):
        """Test cases for the compute_median function."""
        self.assertEqual(compute_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(compute_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(compute_median([-1, 0, 1, 2, 3]), 1)
        self.assertIsNone(compute_median([]))  # Empty list

    def test_compute_mode(self):
        """Test cases for the compute_mode function."""
        self.assertEqual(compute_mode([1, 2, 2, 3, 3, 3, 4]), 3)
        self.assertEqual(compute_mode([3, 3, 3, 4, 4, 5, 5]), 3)
        self.assertIsNone(compute_mode([1, 2, 3, 4, 5]))  # No mode
        self.assertIsNone(compute_mode([]))  # Empty list

    def test_compute_range(self):
        """Test cases for the compute_range function."""
        self.assertEqual(compute_range([1, 2, 3, 4, 5]), 4)
        self.assertEqual(compute_range([10, 20, 30, 40, 50]), 40)
        self.assertEqual(compute_range([-5, 0, 5]), 10)
        self.assertIsNone(compute_range([]))  # Empty list

    def test_edge_cases(self):
        """Test edge cases across all functions."""
        edge_case_data = {
            "empty": [],
            "single": [42],
            "negative": [-5, -10, -15],
            "repeating": [1, 2, 2, 3, 3, 3, 4],
        }

        # Testing compute_mean
        self.assertIsNone(compute_mean(edge_case_data["empty"]))
        self.assertEqual(compute_mean(edge_case_data["single"]), 42)
        self.assertEqual(compute_mean(edge_case_data["negative"]), -10)
        self.assertEqual(compute_mean(edge_case_data["repeating"]), 2.5714285714285716)

        # Testing compute_median
        self.assertIsNone(compute_median(edge_case_data["empty"]))
        self.assertEqual(compute_median(edge_case_data["single"]), 42)
        self.assertEqual(compute_median(edge_case_data["negative"]), -10)
        self.assertEqual(compute_median(edge_case_data["repeating"]), 3)

        # Testing compute_mode
        self.assertIsNone(compute_mode(edge_case_data["empty"]))
        self.assertEqual(compute_mode(edge_case_data["single"]), 42)
        self.assertIsNone(compute_mode(edge_case_data["negative"]))  # No mode
        self.assertEqual(compute_mode(edge_case_data["repeating"]), 3)

        # Testing compute_range
        self.assertIsNone(compute_range(edge_case_data["empty"]))
        self.assertEqual(compute_range(edge_case_data["single"]), 0)
        self.assertEqual(compute_range(edge_case_data["negative"]), 10)
        self.assertEqual(compute_range(edge_case_data["repeating"]), 3)


if __name__ == "__main__":
    unittest.main()
