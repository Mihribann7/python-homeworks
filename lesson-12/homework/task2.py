import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

URL = "https://realpython.github.io/fake-jobs"

DB_NAME = "jobs.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        company TEXT,
                        location TEXT,
                        description TEXT,
                        link TEXT,
                        UNIQUE(title, company, location)
                    )''')
    conn.commit()
    conn.close()


def scrape_jobs():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="description").text.strip()
        link = job.find("a", text="Apply")["href"]

        jobs.append((title, company, location, description, link))

    return jobs


def store_jobs(jobs):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for job in jobs:
        title, company, location, description, link = job
        cursor.execute('''INSERT INTO jobs (title, company, location, description, link)
                          VALUES (?, ?, ?, ?, ?)
                          ON CONFLICT(title, company, location) 
                          DO UPDATE SET description=excluded.description, link=excluded.link''',
                       (title, company, location, description, link))

    conn.commit()
    conn.close()


def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)

    if company:
        query += " AND company = ?"
        params.append(company)

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results


def export_to_csv(filename="filtered_jobs.csv", location=None, company=None):
    jobs = filter_jobs(location, company)

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)

    print(f"Filtered jobs exported to {filename}")


if __name__ == "__main__":
    create_database()
    jobs = scrape_jobs()
    store_jobs(jobs)
    print("Jobs stored successfully.")

    export_to_csv(location="Remote")
