"""BOG Scraper."""

from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup, Tag

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchAttributeException,
    NoSuchElementException,
)
import os
import dotenv
import time

# Constants
dotenv.load_dotenv()
URL = os.getenv("URL")


class Scraper:
    """Scraper class."""

    def __init__(self) -> None:
        """Initializes a headless chrome browser and logs in to a website."""

        s = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=s, options=options)

        try:
            self.driver.get(URL)
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "table_1"))
            )
            time.sleep(3)
            self.content = self.driver.page_source
            self.soup = BeautifulSoup(self.content, "lxml")
        except (NoSuchElementException, NoSuchAttributeException) as e:
            print("Error. Couldn't find element. Please try again.", e)

        except Exception as e:
            print("An error occurred. Please try again.", e)

    def extract_issue_date(self) -> List[str]:
        issue_dates: List[Tag] = self.soup.find_all(
            "td", class_="column-dt_issue_date sorting_1"
        )
        return [date.get_text(strip=True) for date in issue_dates]

    def extract_security_type(self) -> List[str]:
        security_types: List[Tag] = self.soup.find_all(
            "td", class_="column-ds_security_type"
        )
        return [security_type.get_text(strip=True) for security_type in security_types]

    def extract_interest_rate(self) -> List[str]:
        interest_rates: List[Tag] = self.soup.find_all(
            "td", class_="column-vl_interest_rate"
        )
        return [interest_rate.get_text(strip=True) for interest_rate in interest_rates]

    def get_treasury_bills_data(self) -> List[dict]:
        """Return a list of treasury bills."""
        issue_dates = self.extract_issue_date()
        security_types = self.extract_security_type()
        interest_rates = self.extract_interest_rate()

        return [
            {"issue_date": date, "security_type": type, "interest_rate": rate}
            for date, type, rate in zip(issue_dates, security_types, interest_rates)
        ]


if __name__ == "__main__":
    scraper = Scraper()
    bills = scraper.get_treasury_bills_data()
    for bill in bills:
        print(bill)
