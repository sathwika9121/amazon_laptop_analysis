# 💻 Amazon Laptop Market Analysis

This project is a complete data pipeline that automates the process of finding the best laptop deals on Amazon. It handles everything from gathering live data to generating market insights.

---

## 🚀 How It Works (The 3-Step Factory)

### 1. The Collector (`amazon_scraping.py`)
* **Role:** A digital robot powered by **Selenium**.
* **Action:** It opens Amazon, searches for laptops, and automatically scrapes the **Title**, **Price**, and **Rating**.
* **Output:** Saves the raw, messy data into `amazon_laptop_raw.csv`.

### 2. The Cleaner (Pandas Logic)
* **Role:** A data refiner using the **Pandas** library.
* **Action:** It cleans the "dirty" web data by removing currency symbols (₹), fixing commas in prices, and handling missing values.
* **Output:** Saves a "ready-to-use" file called `amazon_laptop_cleaned.csv`.

### 3. The Brain (`analysis.py`)
* **Role:** The data analyst.
* **Action:** It reads the cleaned data to calculate the **Average Price per Brand**, **Top-Rated Laptops**, and **Price vs. Rating correlations**.
* **Output:** Prints a summary of the best-value laptops directly to the terminal.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `amazon_scraping.py` | Python script to collect live data from Amazon. |
| `analysis.py` | Python script to perform data analysis and statistics. |
| `amazon_laptop_raw.csv` | The initial dataset containing raw web data. |
| `amazon_laptop_cleaned.csv` | The final dataset processed for analysis. |

---

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Selenium (Scraping), Pandas (Cleaning & Analysis)
