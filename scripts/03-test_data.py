#### Preamble ####
# Purpose: Tests for "n/a" Replacement and Negative Numbers.
# Author: Vivian Guo
# Date: 23 September 2024
# Contact: vivian.guo@mail.utoronto.ca
# License: N/A
# Pre-requisites: N/A

#### Workspace setup ####
import pandas as pd

#### Test data ####

# Test 1: Check for "n/a" Replacement
def test_na_replacement(df, df_name):
    # Check if any 'n/a' strings remain in the data
    has_na = (df == "n/a").any().any()

    if not has_na:
        print(f"Test 1 Passed: All 'n/a' values have been replaced with 0 in {df_name}.")
    else:
        print(f"Test 1 Failed: Some 'n/a' values remain in the data in {df_name}.")

# Run Test 1
test_na_replacement(cleaned_avg_age_death_data, "cleaned_avg_age_death_data")
test_na_replacement(cleaned_death_data, "cleaned_death_data")

# Test 2: Check for Negative Numbers in cleaned_avg_age_death_data
def test_negative_numbers_avg_age(df):
    numeric_columns = [
        "total_decedents",
        "Average_age_of_death_all_decedents",
        "Male_decedents",
        "Average_age_of_death_male_decedents",
        "Female_decedents",
        "Average_age_of_death_female_decedents",
        "Transgender_Non_binary_Two_Spirit_decedents",
        "Avg_age_of_death_transgender_non_binary_two_spirit_decedents"
    ]

    has_negative = (df[numeric_columns] < 0).any().any()

    if not has_negative:
        print("Negative Number Test Passed: No negative values found in the relevant columns (avg age dataset).")
    else:
        print("Negative Number Test Failed: Negative values found in the relevant columns (avg age dataset).")

# Run Test 2 on avg age dataset
test_negative_numbers_avg_age(cleaned_avg_age_death_data)

# Test 2: Check for Negative Numbers in cleaned_death_data
def test_negative_numbers_deaths(df):
    numeric_columns = [
        "total_decedents",
        "male",
        "female",
        "transgender_nonbinary_twospirit"
    ]

    has_negative = (df[numeric_columns] < 0).any().any()

    if not has_negative:
        print("Negative Number Test Passed: No negative values found in the relevant columns (death count dataset).")
    else:
        print("Negative Number Test Failed: Negative values found in the relevant columns (death count dataset).")

# Run Test 2 on death count dataset
test_negative_numbers_deaths(cleaned_death_data)
