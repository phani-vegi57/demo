#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


#importing data from the local file
dataset1 = pd.read_csv("C:\Data Analysis\Excel Datasets\MapUp Assesment\dataset-1.csv")
dataset2 = pd.read_csv("C:\Data Analysis\Excel Datasets\MapUp Assesment\dataset-2.csv")
dataset3 = pd.read_csv("C:\Data Analysis\Excel Datasets\MapUp Assesment\dataset-3.csv")


# In[10]:


#Printing Dataset-1
dataset1.head()


# In[6]:


#Printing Dataset-2
dataset2.head()


# In[7]:


#Printing Dataset-3
dataset3.head()


# # Question 1: Distance Matrix Calculation
# Create a function named calculate_distance_matrix that takes the dataset-3.csv as input and generates a DataFrame representing distances between IDs.
# 
# The resulting DataFrame should have cumulative distances along known routes, with diagonal values set to 0. If distances between toll locations A to B and B to C are known, then the distance from A to C should be the sum of these distances. Ensure the matrix is symmetric, accounting for bidirectional distances between toll locations (i.e. A to B is equal to B to A).

# In[14]:


import pandas as pd

def generate_car_matrix(dataset):
    # Read the dataset into a DataFrame
    df = pd.read_csv(dataset)
    
    # Pivot the DataFrame to create the car matrix
    car_matrix = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)
    
    # Set diagonal values to 0
    car_matrix.values[[range(len(car_matrix.index))], [range(len(car_matrix.index))]] = 0
    
    return car_matrix

# Example usage
dataset_path = r"C:\Data Analysis\Excel Datasets\MapUp Assesment\dataset-1.csv"
resulting_car_matrix = generate_car_matrix(dataset_path)
print(resulting_car_matrix)


# # Question 2: Car Type Count Calculation
# Create a Python function named get_type_count that takes the dataset-1.csv as a DataFrame. Add a new categorical column car_type based on values of the column car:
# 
# low for values less than or equal to 15,
# medium for values greater than 15 and less than or equal to 25,
# high for values greater than 25.
# Calculate the count of occurrences for each car_type category and return the result as a dictionary. Sort the dictionary alphabetically based on keys.

# In[15]:


import pandas as pd

def get_type_count(dataset):
    # Read the dataset into a DataFrame
    df = pd.read_csv(dataset)
    
    # Add a new categorical column 'car_type' based on the values of the 'car' column
    conditions = [
        (df['car'] <= 15),
        ((df['car'] > 15) & (df['car'] <= 25)),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices)
    
    # Calculate the count of occurrences for each 'car_type' category
    type_count = df['car_type'].value_counts().to_dict()
    
    # Sort the dictionary alphabetically based on keys
    type_count = dict(sorted(type_count.items()))
    
    return type_count

dataset_path = r'C:\Data Analysis\Excel Datasets\MapUp Assesment\dataset-1.csv'
resulting_type_count = get_type_count(dataset_path)
print(resulting_type_count)


# # Question 3: Bus Count Index Retrieval
# Create a Python function named get_bus_indexes that takes the dataset-1.csv as a DataFrame. The function should identify and return the indices as a list (sorted in ascending order) where the bus values are greater than twice the mean value of the bus column in the DataFrame.

# In[17]:


import pandas as pd

def get_bus_indexes(dataset1):
    # Read the dataset into a DataFrame
    df = pd.read_csv(dataset1)
    
    # Calculate the mean value of the 'bus' column
    bus_mean = df['bus'].mean()
    
    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    
    # Sort the indices in ascending order
    bus_indexes.sort()
    
    return bus_indexes

# Example usage
dataset_path = r'C:\Data Analysis\Excel Datasets\MapUp Assesment\dataset-1.csv'
resulting_bus_indexes = get_bus_indexes(dataset_path)
print(resulting_bus_indexes)


# # Question 5: Matrix Value Modification
# Create a Python function named multiply_matrix that takes the resulting DataFrame from Question 1, as input and modifies each value according to the following logic:
# 
# If a value in the DataFrame is greater than 20, multiply those values by 0.75,
# If a value is 20 or less, multiply those values by 1.25.
# The function should return the modified DataFrame which has values rounded to 1 decimal place.

# In[26]:


import pandas as pd

# Assuming the resulting DataFrame from Question 1 is stored in a variable called 'result_df'
# You may need to adjust the actual variable name based on your code
# result_df = ...

def multiply_matrix(result_df):
    # Apply the specified logic to modify the values in the DataFrame
    modified_df = result_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    
    # Round the values to 1 decimal place
    modified_df = modified_df.round(1)
    
    return modified_df

# Example usage:
dataset_path = r"C:\Data Analysis\Excel Datasets\MapUp Assesment\dataset-1.csv"
resulting_car_matrix = generate_car_matrix(dataset_path)


# Using the multiply_matrix function
modified_result_df = multiply_matrix(resulting_car_matrix)

# Displaying the modified DataFrame
print("Modified DataFrame:")
print(modified_result_df)


# In[ ]:




