import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# -------------------------------
# Configuration
# -------------------------------

BASE_URL = "https://www.scrapethissite.com/pages/forms/?page_num={}"
OUTPUT_PATH = os.path.join("data", "raw", "nhl_data.csv")
TOTAL_PAGES = 24
REQUEST_DELAY = 1  # seconds between requests


# -------------------------------
# Fetch HTML Page
# -------------------------------

def fetch_page(url: str) -> str | None:
    """Send HTTP request and return page HTML."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print(f"[ERROR] Failed to fetch {url}")
        print(error)
        return None


# -------------------------------
# Parse HTML Table
# -------------------------------

def parse_html(html: str) -> pd.DataFrame:
    """Extract table data from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table")
    if table is None:
        print("[WARNING] No table found on page.")
        return pd.DataFrame()

    # Extract headers safely
    header_cells = table.find_all("th")
    headers = [cell.get_text(strip=True) for cell in header_cells]

    data_rows = []

    rows = table.find_all("tr")[1:]  # skip header row
    for row in rows:
        cols = row.find_all("td")
        values = [col.get_text(strip=True) for col in cols]

        if values and len(values) == len(headers):
            data_rows.append(values)

    return pd.DataFrame(data_rows, columns=headers)


# -------------------------------
# Save Dataset
# -------------------------------

def save_data(df: pd.DataFrame, path: str = OUTPUT_PATH) -> None:
    """Save dataframe to CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[SUCCESS] Data saved to → {path}")


# -------------------------------
# Main Scraping Pipeline
# -------------------------------

def run_scraper():
    """Main scraping workflow."""
    all_data = pd.DataFrame()

    print(" Starting Web Scraping...\n")

    for page in range(1, TOTAL_PAGES + 1):
        url = BASE_URL.format(page)
        print(f"Processing page {page}/{TOTAL_PAGES}")

        html = fetch_page(url)

        if html:
            df = parse_html(html)

            if not df.empty:
                all_data = pd.concat([all_data, df], ignore_index=True)
            else:
                print(f"[INFO] Page {page} returned empty data.")

        time.sleep(REQUEST_DELAY)

    if not all_data.empty:
        save_data(all_data)
        print("\n Scraping completed successfully!")
        print(f"Total records collected: {len(all_data)}")
    else:
        print("\n No data collected.")


# -------------------------------
# Script Entry Point
# -------------------------------

if __name__ == "__main__":
    run_scraper()