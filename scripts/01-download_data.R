#### Preamble ####
# Purpose: Downloads and saves the data from [...UPDATE THIS...]
# Author: Mandy He
# Date: 23 September 2024 
# Contact: mandyxy.he@mail.utoronto.ca
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]


#### Workspace setup ####
library(opendatatoronto)
library(tidyverse)
library(dplyr)


#### Download data ####

# get package
package <- show_package("deaths-of-shelter-residents")
package

# get all resources for this package
resources <- list_package_resources("deaths-of-shelter-residents")

# identify datastore resources; by default, Toronto Open Data sets datastore resource format to CSV for non-geospatial and GeoJSON for geospatial resources
datastore_resources <- filter(resources, tolower(format) %in% c('csv', 'geojson'))

# load the Deaths of Shelter Residents data
Num_death_data <- filter(datastore_resources, row_number()==1) %>% get_resource()


# Deaths of Shelter Residents Mean Age
Avg_death_age_data <- filter(datastore_resources, row_number()==2) %>% get_resource()


#### Save data ####
write_csv(Num_death_data, "data/raw_data/Num_death_raw_data.csv") 
write_csv(Avg_death_age_data, "data/raw_data/raw_age_data.csv") 

         
