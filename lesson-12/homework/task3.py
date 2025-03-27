import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.demoblaze.com/"

OUTPUT_FILE = "laptops.json"


def get_laptops_from_page(soup):
    laptops = []
    items = soup.find_all("div", class_="card-block")

    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()

        laptops.append({"name": name, "price": price, "description": description})

    return laptops


def scrape_all_laptops():
    all_laptops = []
    page_number = 1

    while True:
        print(f"Scraping page {page_number}...")
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.text, "html.parser")

        laptops = get_laptops_from_page(soup)
        if not laptops:
            break  # Stop if no more laptops are found

        all_laptops.extend(laptops)

        next_button = soup.find("button", id="next2")
        if not next_button:
            break
        page_number += 1
        time.sleep(2)
    return all_laptops


def save_to_json(data, filename=OUTPUT_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")


# Run the script
if __name__ == "__main__":
    laptops = scrape_all_laptops()
    save_to_json(laptops)
    print("Scraping completed.")
