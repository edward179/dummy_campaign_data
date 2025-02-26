# Dummy Campaign Explanation

## About
The objective which is to clean and prepare the data from the dummy campaign.

## Technical Usage
* Programming language: Python
* Framework: pandas, matplotlib, seaborn, openpyxl

## Dataset

| Column                  | Description                                   | Data Type      |
| :---------------------- | :-------------------------------------------- | :------------- |
| TransactionID           | The unique ID of transaction                  | VARCHAR(30)    |
| CampaignID              | The unique ID of campaign                     | VARCHAR(30)    |
| TransactionDate         | The date of transaction                       | DATE           | 
| CustomerID              | The unique ID of customer                     | VARCHAR(50)    |
| CustomerName            | The customer name                             | VARCHAR(50)    |
| Phone                   | The phone number                              | INT            |
| Email                   | The customer email                            | VARCHAR(50)    |
| Age                     | The customer age                              | INT            |
| Gender                  | The customer gender                           | VARCHAR(30)    |
| Region                  | The location where customer live              | VARCHAR(30)    |
| DrinkType               | The type of drink                             | VARCHAR(30)    |
| Quantity                | The number of each transaction                | INT            |
| UnitPrice               | The price of each transaction                 | DECIMAL(10, 2) |
| TotalSpent              | The total spend/ revenue of each transaction  | DECIMAL(10, 2) |
| Channel                 | The channel which use to buy                  | VARCHAR(30)    |
| PaymentMethod           | The payment method of each transaction        | VARCHAR(30)    |
| Discount                | The discount of each transaction              | FLOAT(11, 9)   |
| LoyaltyPoints           | The point of loyalty customer                 | INT            |


## Approach
The content include 3 main-topics:
A. Overview data
> 1. Check & Handling the **Null/ Missing/ Duplicate** value
> 2. Check the basic statistics to better get understanding the dataset

B. Convert & Standardize the data type
> 1. Datetime format
> 2. Standardizing Phone column into 10 numbers and INVALID
> 3. Convert numeric columns to proper format

C. Extract the `AdditionalInfo` column
> 1. Extract & create the 3 new columns including `PaymentMethod` , `Discount` , `LoyaltyPoints`
> 2. Update the consistent format

D. Export to excel file





