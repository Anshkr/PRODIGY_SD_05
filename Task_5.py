import urllib.request
import re
import csv
import tkinter as tk
from tkinter import messagebox

class SimpleScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Book Scraper (No External Modules)")
        self.root.geometry("400x200")

        tk.Label(root, text="Enter number of pages to scrape:", font=("Arial", 12)).pack(pady=10)

        self.page_entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.page_entry.pack()

        tk.Button(root, text="Scrape Now", command=self.start_scraping, font=("Arial", 12), bg="lightgreen").pack(pady=15)

        self.status_label = tk.Label(root, text="", font=("Arial", 10))
        self.status_label.pack()

    def start_scraping(self):
        try:
            pages = int(self.page_entry.get())
            if pages <= 0:
                raise ValueError
            self.scrape_books(pages)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def scrape_books(self, pages):
        BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
        books = []

        for page in range(1, pages + 1):
            self.status_label.config(text=f"Scraping page {page}...")
            self.root.update_idletasks()

            try:
                url = BASE_URL.format(page)
                with urllib.request.urlopen(url) as response:
                    html = response.read().decode("utf-8")
            except:
                messagebox.showerror("Error", f"Failed to fetch page {page}")
                return

            titles = re.findall(r'title="(.*?)"', html)
            prices = re.findall(r'<p class="price_color">£(.*?)</p>', html)
            ratings = re.findall(r'star-rating ([A-Za-z]+)', html)

            count = min(len(titles), len(prices), len(ratings))
            for i in range(count):
                books.append([titles[i], "£" + prices[i], ratings[i]])

        with open("books.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Rating"])
            writer.writerows(books)

        self.status_label.config(text="")
        messagebox.showinfo("Success", f"✅ Scraped {len(books)} books to 'books.csv'")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleScraperGUI(root)
    root.mainloop()
