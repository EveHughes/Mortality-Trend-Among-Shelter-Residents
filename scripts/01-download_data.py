#### Preamble ####
# Purpose: Downloads and saves the data from Open Data Toronto
# Author: Mandy He
# Date: 23 September 2024
# Contact: mandyxy.he@mail.utoronto.ca
# License: N/A
# Pre-requisites: N/A

	
import requests
from io import StringIO
import pandas as pd
 
# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/
 
# To hit our API, you'll be making requests to:
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
 
# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
url = base_url + "/api/3/action/package_show"
params = { "id": "deaths-of-shelter-residents"}
package = requests.get(url, params = params).json()
 
dataframe = []
# To get resource data:
for idx, resource in enumerate(package["result"]["resources"]):
 
       # for datastore_active resources:
       if resource["datastore_active"]:
 
           # To get all records in CSV format:
           url = base_url + "/datastore/dump/" + resource["id"]
           resource_dump_data = requests.get(url)
           data = pd.read_csv(StringIO(resource_dump_data.text))

           dataframe.append(data)
 
Num_death_data = dataframe[0]
Avg_death_age_data = dataframe[1]


#### Save data ####
Num_death_data.to_csv("data/raw_data/Num_death_raw_data.csv", index = False)
Avg_death_age_data.to_csv("data/raw_data/raw_age_data.csv", index = False)
