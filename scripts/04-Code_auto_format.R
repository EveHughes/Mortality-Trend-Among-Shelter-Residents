# Load the styler package
library(styler)

# Define files to format
files_to_format <- c("scripts/00-simulate_data.R", "scripts/01-download_data.R", "scripts/02-data_cleaning.R",
                     "scripts/03-test_data.R", "paper/paper.qmd")

# Loop through each file and format it
lapply(files_to_format, style_file)
