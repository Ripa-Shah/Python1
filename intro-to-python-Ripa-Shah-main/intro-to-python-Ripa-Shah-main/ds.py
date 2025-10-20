#Author: Ripa Shah
#Date: 09/03/2025
# Homework 1: Introduction to Python
# Complete all tasks as specified. You should implement each function below
# and ensure it meets the requirements described in the docstrings.

# Task 1: Compute the mean of a list of numbers.
def compute_mean(numbers):

    if not numbers or len(numbers)==0:
        return None
    total =sum(numbers)
    mean = total/ len(numbers)
    return mean
    """
    Computes the mean of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The mean of the numbers in the list, or None if the list is empty.
    """
    pass  # Replace this with your implementation

val = [10,20,30,40,50]
calculate_mean = compute_mean(val)
print(f"The mean of {val} is: {compute_mean(val)}")
# Task 2: Compute the median of a list of numbers.
def compute_median(numbers):
    if not numbers or len(numbers) == 0:
        return None
    so=numbers.sort()
    print(numbers)
    length= len(numbers)
    print(length)
    if length % 2 == 0:
        res = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        res = numbers[length // 2]
    return res
    pass  # Replace this with your implementation
val_median = [-1,-2,9,20,34,10]
calculate_median = compute_median(val_median)
print(f"the median of {val_median} is: {calculate_median} or {compute_median(val_median)}")


# Task 3: Compute the mode of a list of numbers.
def compute_mode(numbers):
    """
    Computes the mode of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    int/float: The mode of the numbers in the list, or None if the list is empty.
    """
    
    if not numbers or len(numbers) == 0 or any(n < 0 for n in numbers):
        return None
    else:
        print (f"not an empty list")
    if len(numbers) == 1:
        # print (f"no mode exist")
        return numbers[0]
    else:
        print (f"there is more than one element")
    
    occurrence = {}
    for num in numbers:
        if num in occurrence:
            occurrence[num] += 1
        else:
            occurrence[num] = 1

    # Find the maximum frequency
    max_occurrences = max(occurrence.values())
    return None if all(oc == 1 for oc in occurrence.values()) else max_occurrences
    # # Find all numbers that have the maximum frequency
    # modes = []
    # for num, count in occurrence.items():
    #     if count == max_occurrence:
    #         modes.append(num)
    
    # if len(set(numbers)) == len(numbers):
    #     return []
    
    # if len()


    # # Handle the case where all numbers appear with the same frequency (no clear mode)
    # if len(modes) == len(numbers) and len(set(numbers)) == len(numbers):
    #     return [] # No distinct mode if all numbers are unique
    # elif len(modes) == len(occurrence):
    #     if len(set(numbers)) > 1:
    #         # If all unique numbers have the same frequency (e.g., [1,1,2,2]), all are modes
    #         return sorted(modes)[0] # Return sorted for consistent output
    #     else:
    #         return sorted(modes)[0]
    # else:
    #     return sorted(modes)[0] # Return sorted for consistent output

val_mode = [9,34,45,6,45,36]
calculate_mode = compute_mode(val_mode)
print(f"the mode of {val_mode} is: {calculate_mode}")

    # Example usage:
data1 = [21, 13, 19, 13, 19, 13]
print(f"Modes of {data1}: {compute_mode(data1)}")

data2 = [1, 2, 3, 4, 5]
print(f"Modes of {data2}: {compute_mode(data2)}")

data3 = [7, 7, 8, 8, 9, 9]
print(f"Modes of {data3}: {compute_mode(data3)}")

data4 = [10]
print(f"Modes of {data4}: {compute_mode(data4)}")

data5 = []
print(f"Modes of {data5}: {compute_mode(data5)}")

data6 = [-1,-1,-2,-3]
print(f"Modes of {data6}: {compute_mode(data6)}")
          
pass  # Replace this with your implementation


# Task 4: Handle edge cases for each function.
def test_edge_cases():
    """
    Tests the compute_mean, compute_median, and compute_mode functions on edge cases.

    Cases to test:
    1. Empty list.
    2. List with one number.
    3. List with negative numbers.
    4. List with repeating numbers.
    """
    test_data = {
        "empty": [],
        "single": [42],
        "negative": [-5, -10, -15],
        "repeating": [1, 2, 2, 3, 3, 3, 4],
    }

    # Testing compute_mean
    print("Testing compute_mean...")
    for case, data in test_data.items():
        print(f"{case} case: Input: {data}, Mean: {compute_mean(data)}")

    # Testing compute_median
    print("\nTesting compute_median...")
    for case, data in test_data.items():
        print(f"{case} case: Input: {data}, Median: {compute_median(data)}")

    # Testing compute_mode
    print("\nTesting compute_mode...")
    for case, data in test_data.items():
        print(f"{case} case: Input: {data}, Mode: {compute_mode(data)}")


# Task 5: Implement a custom function to calculate the range of a list of numbers.
def compute_range(numbers):
    """
    Computes the range (difference between max and min) of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The range of the numbers in the list, or None if the list is empty.
    """
    if len(numbers) == 0:
        return None

    max_val =max(numbers)
    min_val= min(numbers)
    data_range=max_val-min_val
    print(f" list of numbers {numbers}")
    print(f"Maximum value is: {max_val}")
    print(f"Minimum value is: {min_val}")
    print(f"Range: {data_range}")
    
    return data_range # Replace this with your implementation
val_range=[12,45,23,53,67]
print(f"values :{val_range}:{compute_range(val_range)}")


# Task 6: Write a function to test all implemented calculations.
def test_calculations():
    """
    Tests compute_mean, compute_median, compute_mode, and compute_range 
    with predefined datasets and prints the results.
    """
    datasets = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50],
        [-1, 0, 1, 2, 3],
        [3, 3, 3, 4, 4, 5, 5],
    ]

    print("Testing all functions with datasets...\n")
    for data in datasets:
        print(f"Dataset: {data}")
        print(f"Mean: {compute_mean(data)}")
        print(f"Median: {compute_median(data)}")
        print(f"Mode: {compute_mode(data)}")
        print(f"Range: {compute_range(data)}")
        print("-" * 30)


# Uncomment the following lines to run the test functions.
# test_edge_cases()
# test_calculations()

#References:
#https://www.geeksforgeeks.org/python/find-median-of-list-in-python/
#https://www.geeksforgeeks.org/python/python-list-sort-method/
#https://www.geeksforgeeks.org/python/finding-mean-median-mode-in-python-without-libraries/