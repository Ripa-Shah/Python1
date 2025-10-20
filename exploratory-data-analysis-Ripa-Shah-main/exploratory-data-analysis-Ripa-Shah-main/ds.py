# HW-02: Data Analysis and Cleaning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Task 1: Load and Inspect a Dataset
# Question: Write a function to load a dataset into a pandas DataFrame.
# - Verify that the DataFrame loads successfully.
# - Handle errors gracefully if the file is missing or unreadable.
current_directory = os.getcwd()
print(current_directory)
#file_path = os.path.join(current_directory, 'data', 'midwest.csv')
def load_csv(file_path):    
    #Loads a CSV file into a pandas DataFrame.
    current_directory = os.getcwd()
    print(current_directory)
    print(f"\nAttempting to load file from: {file_path}")
    try:

        if 'az-county.csv' in file_path:
            #file_path = os.path.join(current_directory,'data','az-county.csv')
            df = pd.read_csv(file_path, encoding = 'iso-8859-1')
        elif 'midwest.csv' in file_path:
            #file_path = os.path.join(current_directory,'data','midwest.csv')
            df = pd.read_csv(file_path, encoding= 'iso-8859-1')
        else:
            raise 'FileNotFoundError(f"File not found: {file_path}")' 
         # Verification step
        if df.empty:
            print(f"The file at '{file_path}' was loaded, but the resulting DataFrame is empty.")
            return None
        
        print(f"Success! DataFrame loaded from {file_path}.")
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    return df
    current_directory = os.getcwd()
print(current_directory)
file_path = os.path.join(current_directory, 'data', 'midwest.csv')
#df=pd.read_csv(file_path, encoding = 'iso-8859-1')
#print(df)
df = load_csv(file_path)
print(df)
file_path = os.path.join(current_directory,'data','az-county.csv')
df = load_csv(file_path)
print(df)
# Task 2: Check Data Quality
# Question: Write a function to return a summary of the dataset, including:
# - Number of rows and columns.
# - Percentage of missing values per column.
# - Data types of each column.
def data_summary(df):
    """
    Provides a summary of the dataset.

    Parameters:
    df (pd.DataFrame): The DataFrame to summarize.

    Returns:
    dict: A dictionary with summary statistics, including:
        - 'shape': Tuple of rows and columns.
        - 'missing_percentage': Percentage of missing values for each column.
        - 'data_types': Data types of each column.
    """
    #df=pd.read_csv(file_path, encoding = 'iso-8859-1')
    #print(df)
    #df = load_csv(file_path)
    if df is None:
        return {
            'Error': "Cannot summarize data. DataFrame is None (file loading failed).",
            'shape': (0, 0),
            'missing_percentage': "N/A",
            'data_types': "N/A"
        }
    #print(df)
    dfcolrow = df.shape
    #print(f"Number of rows: {rows}")
    #print(f"Number of columns: {columns}")
    missing_percentage = (df.isnull().sum() / len(df)) * 100
    #print(f"Missing Percentagee:{missing_percentage}")
    col_dtypes = df.dtypes
    #print(col_dtypes)
    summary = {
        'shape': dfcolrow,
        'missing_percentage': missing_percentage,
        'data_types': col_dtypes
    }
    return summary
    pass  # Replace this with your implementation


print(current_directory)
file_path = os.path.join(current_directory, 'data', 'midwest.csv')
df = load_csv(file_path)
data_summary(df)
print(data_summary(df))
file_path = os.path.join(current_directory,'data','az-county.csv')
df = load_csv(file_path)
data_summary(df)
print(data_summary(df))

# Task 3: Clean Missing Data
# Question: Write a function to clean missing data by:
# - Replacing missing numeric values with the column mean.
# - Replacing missing non-numeric values with the most frequent value in the column.
def clean_missing_data(df):
    """
    Cleans missing data in the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame with missing values.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    df = load_csv(file_path)
    if df is None:
        print(" Cannot clean missing data. Input DataFrame is None.")
        return None
    
    # Create a copy to avoid SettingWithCopyWarning, especially important for cleaning operations
    cleaned_df = df.copy() 
    # Replace missing numeric values with the column mean
    for col in cleaned_df.select_dtypes(include=[np.number]):
        cleaned_df[col].fillna(cleaned_df[col].mean(), inplace=True)
    for col in cleaned_df.select_dtypes(include=['object']):
        cleaned_df[col].fillna(cleaned_df[col].mode()[0], inplace=True)
    return cleaned_df
    #for col in df.select_dtypes(include=[np.number]):
    #    df[col].fillna(df[col].mean(), inplace=True)
    #for col in df.select_dtypes(include=['object']):
    #    df[col].fillna(df[col].mode()[0], inplace=True)
    #return df
#apply cleaning function
cleaned_df_data = df.copy()
print(clean_missing_data(cleaned_df_data))
print("\nMissing values count after cleaning:\n", cleaned_df_data.isnull().sum())
# Task 4: Check for Outliers
# Question: Write a function to detect outliers in a numeric column using the IQR method.
# - Return a DataFrame of rows containing outliers.
# - Question: Why is the IQR method commonly used for detecting outliers?
def detect_outliers(df, column):
    """
    Detects outliers in a numeric column using the IQR method.

    Parameters:
    df (pd.DataFrame): The DataFrame to check for outliers.
    column (str): The column to analyze.

    Returns:
    pd.DataFrame: A DataFrame containing rows with outliers.
    """
    df = load_csv(file_path)
    for column in df.select_dtypes(include=np.number).columns:
        q25 = df[column].quantile(0.25)
        q75 = df[column].quantile(0.75)
        iqr = q75 - q25
        lower_bound = q25 - 1.5 * iqr
        upper_bound = q75 + 1.5 * iqr
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        print(f"{column}: {outliers.shape[0]} outliers")
    return df,outliers
    pass  # Replace this with your implementation
print(df)
print(detect_outliers(df,df.poptotal))
## - Question: Why is the IQR method commonly used for detecting outliers?
#1. It is easy to vizualize
#Unlike the mean and standard deviation, which can be distorted by outliers, the IQR is based on 
# ranks and percentiles, so it remains stable.
# Select numerical columns
#numerical_cols = df.select_dtypes(include = ['number']).columns
#for col in numerical_cols:
    # Find Q1, Q3, and interquartile range (IQR) for each column
#    Q1 = df[col].quantile(0.25)
#    Q3 = df[col].quantile(0.75)
#    IQR = Q3 - Q1
#    # Upper and lower bounds for each column
#    lower_bound = Q1 - 1.5 * IQR
#    upper_bound = Q3 + 1.5 * IQR
    # Filter out the outliers from the DataFrame
#    df_clean = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
# Count missing values in each column
#df.isnull().sum()
# Task 5: Visualize Numeric Columns
# Question: Write a function to visualize a numeric column as a histogram.
# - Include labels for the x-axis, y-axis, and a title.
def visualize_column(df, column, title="Column Distribution"):
    """
    Creates a histogram to visualize the distribution of a numeric column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the column.
    column (str): The column to visualize.
    title (str): The title of the plot.

    Returns:
    None
    """
    df = load_csv(file_path)
     # 1. Check if the column exists and is numeric
    if column not in df.columns:
        print(f"Error: Column '{column}' not found in the DataFrame.")
        return
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(f"Error: Column '{column}' is not a numeric type. It is of type {df[column].dtype}.")
        return
    # 2. Create the histogram
    # 2. Create the histogram
    plt.figure(figsize=(10, 6)) # Set a good figure size
    sns.histplot(data=df, x=column, y=df['county'], bins = 15, color = '#2c7bb6', kde=True)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(column, fontsize=12)
    plt.ylabel("Frequency (Count)", fontsize=12)
    
    # Improve aesthetics: remove the top and right spines
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    # 4. Display the plot
    plt.show()
    pass  # Replace this with your implementation
print(visualize_column(df,column='poptotal',title="Population distributioon"))