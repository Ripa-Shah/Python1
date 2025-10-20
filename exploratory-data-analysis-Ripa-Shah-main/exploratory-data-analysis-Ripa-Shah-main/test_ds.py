import unittest
import pandas as pd
import numpy as np
from ds import load_csv, data_summary, clean_missing_data, detect_outliers, visualize_column

class TestDataScienceFunctions(unittest.TestCase):

    def setUp(self):
        # Load provided datasets
        self.az_county_path = "data/az-county.csv"
        self.midwest_path = "data/midwest.csv"
        self.az_county_df = load_csv(self.az_county_path)
        self.midwest_df = load_csv(self.midwest_path)

    # Task 1: Test load_csv
    def test_load_csv(self):
        # Test AZ County dataset
        self.assertIsInstance(self.az_county_df, pd.DataFrame)
        self.assertGreater(len(self.az_county_df), 0)

        # Test Midwest dataset
        self.assertIsInstance(self.midwest_df, pd.DataFrame)
        self.assertGreater(len(self.midwest_df), 0)

    # Task 2: Test data_summary
    def test_data_summary(self):
        # Test summary for AZ County dataset
        summary = data_summary(self.az_county_df)
        self.assertEqual(summary['shape'], self.az_county_df.shape)
        self.assertTrue((summary['missing_percentage'] >= 0).all())
        self.assertTrue((summary['missing_percentage'] <= 100).all())

        # Test summary for Midwest dataset
        summary = data_summary(self.midwest_df)
        self.assertEqual(summary['shape'], self.midwest_df.shape)
        self.assertTrue((summary['missing_percentage'] >= 0).all())
        self.assertTrue((summary['missing_percentage'] <= 100).all())

    # Task 3: Test clean_missing_data
    def test_clean_missing_data(self):
        # Clean AZ County dataset
        cleaned_az_df = clean_missing_data(self.az_county_df)
        self.assertFalse(cleaned_az_df.isnull().any().any())  # Ensure no missing values remain

        # Clean Midwest dataset
        cleaned_midwest_df = clean_missing_data(self.midwest_df)
        self.assertFalse(cleaned_midwest_df.isnull().any().any())  # Ensure no missing values remain

    # Task 4: Test detect_outliers
    def test_detect_outliers(self):
        # Detect outliers in AZ County population
        az_outliers = detect_outliers(self.az_county_df, "population")
        self.assertTrue(len(az_outliers) >= 0)  # Ensure it runs and returns a DataFrame

        # Detect outliers in Midwest popdensity
        midwest_outliers = detect_outliers(self.midwest_df, "popdensity")
        self.assertTrue(len(midwest_outliers) >= 0)  # Ensure it runs and returns a DataFrame

    # Task 5: Test visualize_column
    def test_visualize_column(self):
        # Visualize a column in AZ County dataset
        try:
            visualize_column(self.az_county_df, "population", "Population Distribution in AZ County")
        except Exception as e:
            self.fail(f"visualize_column raised an exception for AZ County: {e}")

        # Visualize a column in Midwest dataset
        try:
            visualize_column(self.midwest_df, "popdensity", "Population Density Distribution in Midwest")
        except Exception as e:
            self.fail(f"visualize_column raised an exception for Midwest: {e}")


if __name__ == "__main__":
    unittest.main()
