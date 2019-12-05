from bs4 import BeautifulSoup
import requests
from Event import Event
from typing import Dict

"""
Python Requsts Library
1. URL: String "www.twitter.com"
2. RESPONSE: get(URL)
3. CONTENT: BeautifulSoup(response.content, "html.parser")
"""


class Calendar(object):
    """
    ===Description===
    A calendar object holding all events
    ===Instance variables===
    important_dates: A dictionary containing all important dates
    """
    def __init__(self, important_dates: Dict):
        self.important_dates = important_dates

    def get_month_event(self, month) -> list:
        """Returning the important dates by month"""
        month = month.lower()
        month = month[0].upper() + month[1:]
        # events = 'events': [event.get_packaged_data() for event in self.important_dates[month]]}
        return [event.get_packaged_data() for event in self.important_dates[month]]

    def get_all_events(self) -> list:
        """Returning all important dates"""
        event_lst = []
        for month in self.important_dates:
            event_lst.extend(self.important_dates[month])
        # events = {'events': [event.get_packaged_data() for event in event_lst]}
        return [event.get_packaged_data() for event in event_lst]


class WebScraper(object):
    """
    ===Description===
    A web scraper designed to grab all information from the UTM important dates website
    ===Instance variables===
    importanDates: A dictionary holding all important dates categorized by months
    """
    def __init__(self):
        self.url = 'https://student.utm.utoronto.ca/importantDates/importantDates.php'
        self.importantDates = {"January": [], "February": [], "March": [],
                               "April": [], "May": [], "June": [],
                               "July": [], "August": [], "September": [],
                               "October": [], "November": [], "December": []}

    def start_scrape(self) -> None:
        """Starts scraping the UTM website to gather all necessary information"""
        response = requests.get(self.url, timeout=5)
        content = BeautifulSoup(response.content, "html.parser")
        for date in content.findAll('div', attrs={"class": "date"}):
            datetime = str(date.find('h3', attrs={}).text).replace(",", '').replace("-", "").split()
            info = str(date.find('div', attrs={"class": "info"}).text).replace('\xa0', ' ')
            if len(datetime) == 3:
                event = Event(int(datetime[2]), datetime[0], int(datetime[1]), info)
            else:
                event = Event(int(datetime[2]), datetime[0], int(datetime[1]), info, int(datetime[5]), datetime[3],
                              int(datetime[4]))
                # self.set_important_date(datetime[3], event)
            self.set_important_date(datetime[0], event)

    def get_important_dates(self) -> Dict:
        """Returns the dictionary of an event"""
        return self.importantDates

    def set_important_date(self, month: str, event: Event) -> None:
        """Stores the event categorized by month"""
        self.importantDates[month].append(event)
