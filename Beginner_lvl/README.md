# 📊 Retail Sales Performance Analysis

## 📌 Project Overview

This project focuses on analyzing an Online Retail dataset to understand sales performance, customer behavior, revenue trends, and product performance.

The project includes data cleaning, exploratory analysis, Pivot Tables, and an interactive-style Excel dashboard to present important business insights in a clear and visual manner.

---

## 🎯 Objective

The main objectives of this project are:

- Clean and prepare the raw retail sales dataset.
- Remove duplicate and unnecessary records.
- Analyze sales and revenue performance.
- Identify top-performing countries.
- Identify top-performing products.
- Identify high-value customers.
- Analyze monthly revenue trends.
- Create a dashboard containing important KPIs and visualizations.

---

## 🗂️ Dataset

The dataset used in this project is an **Online Retail Dataset** containing transaction-level retail sales information.

### Important Columns

| Column | Description |
|---|---|
| InvoiceNo | Unique invoice/transaction number |
| StockCode | Product identification code |
| Description | Product description |
| Quantity | Number of items purchased |
| InvoiceDate | Date and time of transaction |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identification number |
| Country | Customer's country |
| Revenue | Calculated revenue from the transaction |

### Revenue Calculation

Revenue was calculated using:

**Revenue = Quantity × UnitPrice**

---

## 🧹 Data Cleaning

The following data cleaning activities were performed:

- Removed duplicate records.
- Checked and handled missing/invalid values.
- Reviewed transaction data for consistency.
- Created a calculated **Revenue** field.
- Created additional date-related fields such as:
  - Month-Year
  - Year
  - Month Number
- Prepared the cleaned dataset for analysis.

---

## 📈 Analysis Performed

The project analyzes the following key areas:

### 1. Overall Sales Performance

Key Performance Indicators (KPIs):

- Total Revenue
- Total Quantity Sold
- Total Orders
- Unique Customers
- Average Order Value

### 2. Monthly Revenue Trend

Analyzed revenue across different months to understand sales patterns and identify periods of higher and lower performance.

### 3. Top 10 Countries by Revenue

Identified the countries generating the highest amount of revenue.

### 4. Top 10 Products by Revenue

Identified the products contributing the most to overall revenue.

### 5. Top 10 Customers by Revenue

Identified customers with the highest contribution to total revenue.

---

## 📊 Dashboard

A dedicated Excel dashboard was created to summarize the analysis.

The dashboard includes:

- Total Revenue
- Total Quantity
- Total Orders
- Unique Customers
- Average Order Value
- Monthly Revenue Trend
- Top 10 Countries by Revenue
- Top 10 Products by Revenue
- Top 10 Customers by Revenue

The dashboard provides a simple visual overview of the business performance and helps in understanding important sales trends.

---

## 🛠️ Tools & Technologies

- **Microsoft Excel**
- Pivot Tables
- Pivot Charts
- Excel formulas
- Data Cleaning
- Data Analysis
- Data Visualization

---

## 📁 Project Structure

```text
ShadowFox_DataAnalyst/
│
└── Beginner_lvl/
    │
    ├── Online_Retail_Dataset.xlsx
    └── README.md
