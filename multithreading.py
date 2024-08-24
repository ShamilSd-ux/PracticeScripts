import requests
from bs4 import BeautifulSoup
import threading
import sqlite3

# Function to fetch and parse a webpage
def fetch_and_parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract data (e.g., product names and prices)
    products = soup.find_all('div', class_='product')
    data = [(p.find('h2').text, p.find('span', class_='price').text) for p in products]
    save_to_db(data)

# Function to save data to SQLite database
def save_to_db(data):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", data)
    conn.commit()
    conn.close()

# List of URLs to scrape
urls = ["https://example.com/page1", "https://example.com/page2", ...]

# Create threads
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_and_parse, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
