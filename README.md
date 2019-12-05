# Event-Generator
A UTM Event Generator

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
