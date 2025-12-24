import pandas as pd

# Load the raw CSV in chunks (to handle large size)
chunks = pd.read_csv('C:/Users/Kartik/Desktop/Portfolio Projects/Food_Dashboard/Global WFP Food Prices.csv', chunksize=100000)
data = pd.concat(chunks, ignore_index=True)

# Check column names
print("Columns:", data.columns)

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Drop rows with invalid dates
data = data.dropna(subset=['date'])

# Extract year and month
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

# Use price_usd for uniform currency
data = data.dropna(subset=['price_usd'])

# Aggregate 1: Country-Year-Commodity average price
country_year_agg = data.groupby(['county', 'year', 'commodity'])['price_usd'].mean().reset_index()
country_year_agg.rename(columns={'county': 'Country', 'commodity': 'Commodity', 'price_usd': 'Avg_Price_USD'}, inplace=True)
country_year_agg.to_csv('C:/Users/Kartik/Desktop/Portfolio Projects/Food_Dashboard/avg_prices_by_country_year.csv', index=False)

# Aggregate 2: Global Commodity-Year trend
commodity_year_agg = data.groupby(['commodity', 'year'])['price_usd'].mean().reset_index()
commodity_year_agg.rename(columns={'commodity': 'Commodity', 'price_usd': 'Avg_Price_USD'}, inplace=True)
commodity_year_agg.to_csv('C:/Users/Kartik/Desktop/Portfolio Projects/Food_Dashboard/commodity_global_trends.csv', index=False)

# Optional: Calculate volatility per commodity-country
volatility = data.groupby(['county', 'commodity'])['price_usd'].std().reset_index()
volatility.rename(columns={'county': 'Country', 'commodity': 'Commodity', 'price_usd': 'Price_STD'}, inplace=True)
volatility.to_csv('C:/Users/Kartik/Desktop/Portfolio Projects/Food_Dashboard/commodity_country_volatility.csv', index=False)

print("Preprocessing done! Files saved!")
