#### Preamble ####
# Purpose: Simulates a sample data of Deaths Among Shelter Residents from 2007 to 2024
# Author: Vivian Guo
# Date: 23 September 2024
# Contact: vivian.guo@mail.utoronto.ca
# License: N/A
# Pre-requisites: N/A

#### Workspace setup ####
import pandas as pd
import numpy as np
import os

#### Simulate data ####
np.random.seed(304)

# Set parameters for the simulation
start_year = 2007
end_year = 2024
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Initialize an empty list to hold the data
data = []

# Loop through the years and months to generate data
for year in range(start_year, end_year + 1):
    for month in months:
        # Randomly determine the total number of decedents for the month
        total_decedents = np.random.poisson(lam=2)

        # Ensure total decedents is not negative
        total_decedents = max(total_decedents, 0)

        # Randomly assign gender categories based on proportions
        if total_decedents > 0:
            male = np.random.randint(0, total_decedents + 1)  # Random number of males
            female = total_decedents - male  # Remainder are females
            transgender_non_binary = np.random.randint(0, 2)  # 0 or 1
        else:
            male = female = transgender_non_binary = 0

        # Append the new row to the data list
        data.append({
            "id": len(data) + 1,
            "Year": year,
            "Month": month,
            "Total_decedents": total_decedents,
            "Male": male,
            "Female": female,
            "Transgender_Non_binary_Two_Spirit": transgender_non_binary
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the simulated data
print(df.head())

# Create the directory if it doesn't exist
os.makedirs("data/raw_data", exist_ok=True)

# Write the data to CSV
df.to_csv("data/raw_data/simulated.csv", index=False)
