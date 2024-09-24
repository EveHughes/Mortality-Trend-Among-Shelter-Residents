#### Preamble ####
# Purpose: Tests... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 11 February 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]


#### Workspace setup ####
library(tidyverse)
# [...UPDATE THIS...]

#### Test data ####

# Test 1: Check for "n/a" Replacement
test_na_replacement <- function(cleaned_avg_age_death_data) {
  # Check if any "n/a" values remain in the data
  has_na <- any(cleaned_avg_age_death_data == "n/a")
  
  if (!has_na) {
    print("Test 1 Passed: All 'n/a' values have been replaced with 0.")
  } else {
    print("Test 1 Failed: Some 'n/a' values remain in the data.")
  }
}

# Run Test 1
test_na_replacement(cleaned_avg_age_death_data)
test_na_replacement(cleaned_death_data)


# Test2: Check for Negative Numbers
test_negative_numbers <- function(cleaned_avg_age_death_data) {
  # Define the relevant columns to check for negative numbers
  numeric_columns <- c(
    "Total decedents",
    "Average age of death, all decedents",
    "Male decedents",
    "Average age of death, male decedents",
    "Female decedents",
    "Average age of death, female decedents",
    "Transgender/Non-binary/Two-Spirit decedents",
    "Avg age of death, transgender/non-binary/two-spirit decedents"
  )
  
  # Check for negative values in the specified columns
  has_negative <- any(sapply(cleaned_avg_age_death_data[numeric_columns], function(x) any(x < 0)))
  
  if (!has_negative) {
    print("Negative Number Test Passed: No negative values found in the relevant columns.")
  } else {
    print("Negative Number Test Failed: Negative values found in the relevant columns.")
  }
}

# Run the Negative Number Test
test_negative_numbers(cleaned_avg_age_death_data)


# Test2: Check for Negative Numbers
test_negative_numbers <- function(cleaned_death_data) {
  # Define the relevant columns to check for negative numbers
  numeric_columns <- c(
    "Total decedents",
    "Male",
    "Female",
    "Transgender/Non-binary/Two-Spirit"
  )
  
  # Check for negative values in the specified columns
  has_negative <- any(sapply(cleaned_death_data[numeric_columns], function(x) any(x < 0)))
  
  if (!has_negative) {
    print("Negative Number Test Passed: No negative values found in the relevant columns.")
  } else {
    print("Negative Number Test Failed: Negative values found in the relevant columns.")
  }
}

# Run the Negative Number Test
test_negative_numbers(cleaned_death_data)