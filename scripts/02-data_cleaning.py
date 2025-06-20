#### Preamble ####
# Purpose: Cleans the raw data so variable is easier to call
# Author: Mandy He
# Date: 23 September 2024
# Contact: mandyxy.he@mail.utoronto.ca
# License: N/A
# Pre-requisites: N/A

#### Workspace setup ####
import pandas as pd
from datetime import datetime

#### Clean data ####

## Clean the number of death data first
raw_death_data = pd.read_csv("data/raw_data/Num_death_raw_data.csv")

# Display the first few rows of the original data set
print(raw_death_data.head())

# Clean the data
cleaned_death_data = raw_death_data.rename(columns={
    "_id": "id",
    "Year": "year",
    "Month": "month",
    "Total decedents": "total_decedents",
    "Male": "male",
    "Female": "female",
    "Transgender/Non-binary/Two-Spirit": "transgender_nonbinary_twospirit"
})

# Replace "n/a" / null with 0 in all columns
cleaned_death_data = cleaned_death_data.applymap(
    lambda x: x if pd.notna(x) else 0
)

# Convert relevant columns to proper data types
cleaned_death_data["id"] = cleaned_death_data["id"].astype(int)
cleaned_death_data["year"] = cleaned_death_data["year"].astype(int)
cleaned_death_data["month"] = cleaned_death_data["month"].astype(str)
cleaned_death_data["total_decedents"] = cleaned_death_data["total_decedents"].astype(int)
cleaned_death_data["male"] = cleaned_death_data["male"].astype(int)
cleaned_death_data["female"] = cleaned_death_data["female"].astype(int)
cleaned_death_data["transgender_nonbinary_twospirit"] = cleaned_death_data["transgender_nonbinary_twospirit"].astype(int)

# Display the cleaned dataset
print(cleaned_death_data.head())

#remove rows after September 2024
cleaned_death_data = cleaned_death_data[
    ~(
        (cleaned_death_data["year"] == 2025) |
        ((cleaned_death_data["year"] == 2024) & (cleaned_death_data["month"].isin(["Oct", "Nov", "Dec"])))
    )
]

## Clean the Average age of death data
raw_age_data = pd.read_csv("data/raw_data/raw_age_data.csv")

# Display the first few rows of the original dataset
print(raw_age_data.head())

# Clean the data
cleaned_avg_age_death_data = raw_age_data.rename(columns={
    "_id": "id",
    "Year": "year",
    "Total decedents": "total_decedents",
    "Average age of death, all decedents": "Average_age_of_death_all_decedents",
    "Male decedents": "Male_decedents",
    "Average age of death, male decedents": "Average_age_of_death_male_decedents",
    "Female decedents": "Female_decedents",
    "Average age of death, female decedents": "Average_age_of_death_female_decedents",
    "Transgender/Non-binary/Two-Spirit decedents": "Transgender_Non_binary_Two_Spirit_decedents",
    "Avg age of death, transgender/non-binary/two-spirit decedents": "Avg_age_of_death_transgender_non_binary_two_spirit_decedents"
})

# Replace "n/a" with 0 in all columns
cleaned_avg_age_death_data = cleaned_avg_age_death_data.applymap(
    lambda x: x if pd.notna(x) else 0
)
# Convert relevant columns to numeric types
cleaned_avg_age_death_data["id"] = cleaned_avg_age_death_data["id"].astype(int)

# Convert 'year', including handling "2025 ytd"
cleaned_avg_age_death_data["year"] = cleaned_avg_age_death_data["year"].apply(
    lambda x: 2025 if str(x).strip().lower() == "2025 ytd" else int(x)
)

#remove 2025
cleaned_avg_age_death_data = cleaned_avg_age_death_data[cleaned_avg_age_death_data["year"] < 2025]

cleaned_avg_age_death_data["total_decedents"] = cleaned_avg_age_death_data["total_decedents"].astype(int)
cleaned_avg_age_death_data["Average_age_of_death_all_decedents"] = cleaned_avg_age_death_data["Average_age_of_death_all_decedents"].astype(float)
cleaned_avg_age_death_data["Male_decedents"] = cleaned_avg_age_death_data["Male_decedents"].astype(int)
cleaned_avg_age_death_data["Average_age_of_death_male_decedents"] = cleaned_avg_age_death_data["Average_age_of_death_male_decedents"].astype(float)
cleaned_avg_age_death_data["Female_decedents"] = cleaned_avg_age_death_data["Female_decedents"].astype(int)
cleaned_avg_age_death_data["Average_age_of_death_female_decedents"] = cleaned_avg_age_death_data["Average_age_of_death_female_decedents"].astype(float)
cleaned_avg_age_death_data["Transgender_Non_binary_Two_Spirit_decedents"] = cleaned_avg_age_death_data["Transgender_Non_binary_Two_Spirit_decedents"].astype(int)
cleaned_avg_age_death_data["Avg_age_of_death_transgender_non_binary_two_spirit_decedents"] = cleaned_avg_age_death_data["Avg_age_of_death_transgender_non_binary_two_spirit_decedents"].astype(float)

# Display the cleaned data
print(cleaned_avg_age_death_data.head())

#### Save data ####
cleaned_death_data.to_csv("data/analysis_data/Num_death_analysis_data.csv", index=False)
cleaned_avg_age_death_data.to_csv("data/analysis_data/AvgAge_death_analysis_data.csv", index=False)
