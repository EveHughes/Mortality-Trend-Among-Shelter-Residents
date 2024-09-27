#### Preamble ####
# Purpose: Cleans the raw data so variable is easier to call
# Author: Mandy He
# Date: 23 September 2024
# Contact: mandyxy.he@mail.utoronto.ca
# License: N/A
# Pre-requisites: N/A

#### Workspace setup ####
library(tidyverse)
library(dplyr)
library(tidyr)
library(readr)


#### Clean data ####

## clean the number of death data frist
raw_death_data <- read_csv("data/raw_data/Num_death_raw_data.csv")

# Display the first few rows of the original data set
head(raw_death_data)

# Clean the data
cleaned_death_data <- raw_death_data %>%
  # Rename columns to remove spaces and special characters
  rename(
    id = `_id`,
    year = `Year`,
    month = `Month`,
    total_decedents = `Total decedents`,
    male = `Male`,
    female = `Female`,
    transgender_nonbinary_twospirit = `Transgender/Non-binary/Two-Spirit`
  ) %>%
  # Replace "n/a" with 0 in the relevant columns
  mutate(across(everything(), ~ ifelse(. == "n/a", 0, .))) %>%
  # Convert relevant columns to numeric
  mutate(
    id = as.integer(id),
    year = as.integer(year),
    month = as.character(month),
    total_decedents = as.integer(total_decedents),
    male = as.integer(male),
    female = as.integer(female),
    transgender_nonbinary_twospirit = as.integer(transgender_nonbinary_twospirit)
  )

# Display the cleaned dataset
head(cleaned_death_data)

## Clean the Average age of death data.
raw_age_data <- read_csv("data/raw_data/raw_age_data.csv")

# Display the first few rows of the original dataset
head(raw_age_data)

# Clean the data
cleaned_avg_age_death_data <- raw_age_data %>%
  # Rename columns to remove spaces and special characters
  rename(
    id = `_id`,
    year = `Year`,
    total_decedents = `Total decedents`,
    Average_age_of_death_all_decedents = `Average age of death, all decedents`,
    Male_decedents = `Male decedents`,
    Average_age_of_death_male_decedents = `Average age of death, male decedents`,
    Female_decedents = `Female decedents`,
    Average_age_of_death_female_decedents = `Average age of death, female decedents`,
    Transgender_Non_binary_Two_Spirit_decedents = `Transgender/Non-binary/Two-Spirit decedents`,
    Avg_age_of_death_transgender_non_binary_two_spirit_decedents = `Avg age of death, transgender/non-binary/two-spirit decedents`
  ) %>%
  # Replace "n/a" with 0
  mutate(across(everything(), ~ ifelse(. == "n/a", 0, .))) %>%
  # Convert relevant columns to numeric
  mutate(
    id = as.integer(id),
    year = ifelse(year == "2024 ytd", 2024, as.integer(year)), # Handle '2024 ytd'
    total_decedents = as.integer(total_decedents),
    Average_age_of_death_all_decedents = as.numeric(Average_age_of_death_all_decedents),
    Male_decedents = as.integer(Male_decedents),
    Average_age_of_death_male_decedents = as.numeric(Average_age_of_death_male_decedents),
    Female_decedents = as.integer(Female_decedents),
    Average_age_of_death_female_decedents = as.numeric(Average_age_of_death_female_decedents),
    Transgender_Non_binary_Two_Spirit_decedents = as.integer(Transgender_Non_binary_Two_Spirit_decedents),
    Avg_age_of_death_transgender_non_binary_two_spirit_decedents = as.numeric(Avg_age_of_death_transgender_non_binary_two_spirit_decedents)
  )

# Display the cleaned data
head(cleaned_avg_age_death_data)

#### Save data ####
write_csv(cleaned_death_data, "data/analysis_data/Num_death_analysis_data.csv")
write_csv(cleaned_avg_age_death_data, "data/analysis_data/AvgAge_death_analysis_data.csv")
