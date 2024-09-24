#### Preamble ####
# Purpose: Simulates... [...UPDATE THIS...]
# Author: Mandy He
# Date: 23 September 2024 
# Contact: mandyxy.he@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
# Any other information needed? 


#### Workspace setup ####
library(tidyverse)
library(dplyr)


#### Simulate data ####
set.seed(304)

# Set parameters for the simulation
start_year <- 2007
end_year <- 2024
months <- month.abb  # Built-in R vector for month abbreviations

# Initialize an empty data frame to hold the data
data <- data.frame()

# Loop through the years and months to generate data
for (year in start_year:end_year) {
  for (month in months) {
    # Randomly determine the total number of decedents for the month
    total_decedents <- rpois(1, lambda = 2)  # Using Poisson distribution for count data
    
    # Ensure total decedents is not negative
    total_decedents <- max(total_decedents, 0)
    
    # Randomly assign gender categories based on proportions
    if (total_decedents > 0) {
      male <- sample(0:total_decedents, 1)  # Randomly assign number of males
      female <- total_decedents - male        # The rest will be females
      transgender_non_binary <- sample(0:1, 1)  # Randomly assign Transgender/Non-binary/Two-Spirit
    } else {
      male <- female <- transgender_non_binary <- 0
    }
    
    # Create a new row of data
    new_row <- data.frame(
      id = nrow(data) + 1,
      Year = year,
      Month = month,
      Total_decedents = total_decedents,
      Male = male,
      Female = female,
      Transgender_Non_binary_Two_Spirit = transgender_non_binary
    )
    
    # Append the new row to the data frame
    data <- bind_rows(data, new_row)
  }
}

# Display the first few rows of the simulated data
head(data)


# Create the directory if it doesn't exist
dir.create("data/raw_data", recursive = TRUE)

# Write the data to CSV
write_csv(data, file = "data/raw_data/simulated.csv")


