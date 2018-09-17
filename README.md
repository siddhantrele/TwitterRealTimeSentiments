# TwitterRealTimeSentiments
Django + FusionCharts implementation for real time twitter sentiment tracking

Setup

I would recommend setting up a virtualenv with Python3.6 to avoid compatibility issues.
1. Activate the virtualenv and install required modules from requirements.txt.
2. Open the python shell and run import nltk and nltk.download('vader_lexicon') for Vader Sentiment Analysis
3. Modify scraper_settings.py and enter your Twitter API Keys and the track terms for which sentiments need to be tracked.
4. Execute python manage.py runall. It will run the Twitter Sentiment Scraper alongside the Django Server.

![screenshot](https://user-images.githubusercontent.com/16881337/45599047-b25de900-ba02-11e8-9da9-6e8dca442169.PNG)


