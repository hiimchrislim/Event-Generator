# Event-Generator
A UTM Event Generator

# Description
You'll never miss an important event whether it be course selections or tuition payment with all of the important dates loaded onto your Google calendar!

# How it works
1. Scrape all of the important events from registrar.utm.utoronto.ca/student/importantDates/importantDates.php
(i.e The information about the event and it's associated date)
2. For each event scraped, it's made into an Event object.
3. The event objects are then stored in a Calendar object which sorts all events based on its starting date
4. All events are accessed by the API at localhost:3000 which are categorized by month (In a JSON format)
5. All events are inserted into your Google calendar by accessing the API
6. Enjoy and never worry about missing an important school event!


1. Install the required libraries

- oauth2client
- httplib2
- apiclient
- (Update pip if necessary)

2. Setup oauth2 credentials and api key
https://console.developers.google.com
Setup oauth2 type as "other" with http://localhost (if needed)

3. Run routes.py

4. Start createEventsSample.py

5. Go through the oauth2 prompt, enter your key and enjoy!

---------------------------------------------------------
# API Usage

1. After running routes.py visit http://127.0.0.1:5000/events/ to view all UTM Events for the year

2. To filter out the events by month input the month after /events/ 
(e.g http://127.0.0.1:5000/events/March will return you all the events occuring in March)

3. Enjoy!
