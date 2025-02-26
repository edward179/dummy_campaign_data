import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import json

df = pd.read_csv(io.BytesIO(uploaded['dummy_campaign_data.csv']))

# A. Check Overview data
df.info()
df.head()

## 1. Check basic statistics
df.describe()

## 2. Check for missing value
print(df.isnull().sum())


## 3. Replace missing/ NaN value
df.fillna({'Phone': 'defaul_value'}, inplace=True)
print(df.isnull().sum())


# 4. Handle & Remove duplicate
print("Duplicate Rows: ", df.duplicated().sum())
df.drop_duplicates(inplace=True)


# B. Covert data type
## 1. Datetime format
from datetime import datetime
date_formats = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%b %d, %Y",
    "%Y.%m.%d",
    "%m-%d-%Y",
    "%Y/%m/%d",
    "%B %d, %Y",
    "%d-%m-%Y",
    "%m/%d/%Y"
]

def parse_date(date_str):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return pd.NaT

df['TransactionDate_clean'] = df['TransactionDate'].apply(parse_date)


## 2. Standardizing Phone column into 10 numbers and INVALID
import re

### Function to clean phone numbers
def clean_phone(phone):
    if pd.isna(phone) or phone.strip().upper() == "INVALID":
        return "INVALID"

    phone = re.sub(r'\D', '', str(phone))  # Remove non-numeric characters

    if len(phone) == 10:  # Ensure it's exactly 10 digits
        return phone
    else:
        return "INVALID"  # Mark invalid numbers

### Apply function to Phone column
df['Phone'] = df['Phone'].apply(clean_phone)

### Check results
print(df[['Phone']].head())


## 3. Convert numeric columns to proper format
numeric_columns = [
    'Quantity',
    'UnitPrice',
    'TotalSpent'
]

for col in numeric_columns:
  if col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')


# C. Extract 3 new columns including PaymentMehod, Discount, LoyaltyPoints from the AdditionalInfo column
### Function to safely extract values from JSON-like strings
def extract_json_values(row, key):
    try:
        data = json.loads(row.replace("'", '"'))  # Ensure proper JSON format
        return data.get(key, None)
    except (json.JSONDecodeError, TypeError):
        return None  # Return None for rows that are not valid JSON

### Extract values into new columns
df['PaymentMethod'] = df['AdditionalInfo'].apply(lambda x: extract_json_values(x, 'paymentMethod'))
df['Discount'] = df['AdditionalInfo'].apply(lambda x: extract_json_values(x, 'discount'))
df['LoyaltyPoints'] = df['AdditionalInfo'].apply(lambda x: extract_json_values(x, 'loyaltyPoints'))

### Convert Discount and LoyaltyPoints to numeric
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
df['LoyaltyPoints'] = pd.to_numeric(df['LoyaltyPoints'], errors='coerce')

### Drop the original AdditionalInfo column if it's no longer needed
df.drop(columns=['AdditionalInfo'], inplace=True)

### Preview the result
df[['PaymentMethod', 'Discount', 'LoyaltyPoints']].head()


# D. Export excel file
df.to_excel('cleaned_dummy_campaign_data.xlsx', index=False, engine='openpyxl')

from google.colab import files
files.download('cleaned_dummy_campaign_data.xlsx')



