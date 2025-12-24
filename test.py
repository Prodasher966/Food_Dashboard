import pandas as pd

# Specify the file path
file_path = ('C:/Users/Kartik/Desktop/Portfolio Projects/Food_Dashboard/Global WFP Food Prices.csv')

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Get column names and their types
column_info = df.dtypes

print(column_info)
