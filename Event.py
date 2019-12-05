from datetime import datetime


class Event(object):
    """
    ===Description===
    An event object to represent an event on the UTM important dates calendar
    ===Instance Variables==
    start_date: The start date of the event
    end_date: The end date of the event
    information: The information associated with the event
    months: Containing the months int value
    """

    def __init__(self, start_year, start_month, start_day, information: str, end_year=1, end_month="January",
                 end_day=1):
        self.months = {"January": 1, "February": 2, "March": 3,
                   "April": 4, "May": 5, "June": 6,
                   "July": 7, "August": 8, "September": 9,
                   "October": 10, "November": 11, "December": 12}
        # Can possibly use datetime.strptime("Aug", "%b") -> returns datetime.datetime(1990, 8, 1, 0, 0)
        self.start_date = datetime(start_year, self.months[start_month], start_day)
        self.end_date = datetime(end_year, self.months[end_month], end_day)
        self.information = information

    def get_start_year(self) -> int:
        """Returns the event start year as an int"""
        return self.start_date.year

    def get_start_month(self) -> int:
        """Returns the event start month as an int"""
        return self.start_date.month

    def get_start_day(self) -> int:
        """Returns the event start day as an int"""
        return self.start_date.day

    def get_end_year(self) -> int:
        """Returns the event end year as an int"""
        return self.end_date.year

    def get_end_month(self) -> int:
        """Returns the event end month as an int"""
        return self.end_date.month

    def get_end_day(self) -> int:
        """Returns the event end day as an int"""
        return self.end_date.day

    def get_information(self) -> str:
        """Returns the information of the event"""
        return self.information

    def get_packaged_data(self) -> dict:
        """Returns packaged data of the event in the form of a dict"""
        return {"start_year": self.get_start_year(), "start_month": self.get_start_month(),
                 "start_day": self.get_start_day(), "end_year": self.get_end_year(),
                 "end_month": self.get_end_month(), "end_day": self.get_end_day(),
                 "info": self.get_information()}
