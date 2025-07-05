# PRODIGY_SD_05

# 📚 GUI Book Scraper (No External Modules)

A lightweight GUI-based web scraper built using **only built-in Python modules**.  
It extracts product information (title, price, and rating) from [Books to Scrape](http://books.toscrape.com) and saves the data to a CSV file.

✅ **No installation needed**  
✅ **Beginner-friendly GUI**  
✅ **No external libraries** (pure Python)

---

## 🎯 Features

- 📥 Input number of pages to scrape via GUI
- 🔍 Extracts **Book Title**, **Price**, and **Rating**
- 📄 Stores results in a structured `books.csv` file
- 🧼 Clean, minimal design using `Tkinter`
- 🔁 Uses `urllib` and `re` instead of `requests` or `BeautifulSoup`

---

## 📦 Built With

- `tkinter` – for GUI interface  
- `urllib.request` – for fetching HTML content  
- `re` – for HTML pattern matching (Regex)  
- `csv` – to write data into a `.csv` file

_All of the above are standard Python libraries – no pip install required!_

---

## 🖥️ How to Run

1. **Save the script** as `Task_5.py`

2. **Run the script:**
```bash
python Task_5.py
