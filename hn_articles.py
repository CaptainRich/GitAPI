""" A Script to acquire articles from Hacker-News.com. """

import requests                   # To make API calls to a website
import json                       # To access/format JSON data
from operator import itemgetter   #

# Make an API call to Hacker-News and store the resulting response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get( url )
print( f"Status Code: {r.status_code}" )

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get( url )
    print( f"id: {submission_id}\tStatus: {r.status_code}" )
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'] 
    }
    submission_dicts.append( submission_dict )

    submission_dicts = sorted( submission_dicts, key=itemgetter( 'comments' ),
                              reverse=True )
    
    # Display the information.
    for submission_dict in submission_dicts:
        print( f"\nTitle: {submission_dict['title']} " )
        print( f"Discussion link: {submission_dict['hn_link']}" )
        print( f"Comments: {submission_dict['comments']}" )