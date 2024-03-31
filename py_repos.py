""" A script to query GitHUB python repositories. """

import requests                # To make API calls to a website
from pathlib import Path       # For file I/O
import plotly.express as px    # For visualizing the repo data


# Setup the URL (target) for the request
#language = 'Javascript'
language  = 'Python'

url = "https://api.github.com/search/repositories"
url += "?q=language:"
url += language
url += "+sort:stars+stars:>10000"

headers = { "Accept": "application/vnd.github.v3+json" }
r = requests.get( url, headers=headers )
print( f"\n\nStatus code: {r.status_code}" )

# Convert the response object to a Python dictionary.
response_dict = r.json()

# Process the results (response).
print( response_dict.keys() )
print( f"Total {language} repositories: {response_dict['total_count']}" )
print( f"Complete results: {not response_dict['incomplete_results']}" )

# Report information about the repos.
repo_dicts = response_dict['items']
print( f"Repositories returned: {len(repo_dicts)}" )


""" Depreciated code ...
# Report on the first repo returned.
repo_dict = repo_dicts[0]
print( f"\nKeys: {len(repo_dict)}" ) 

for key in sorted( repo_dict.keys() ):
    print( key )

# Report selected information on this (1st) repo
print( "\nSelected information from the 1st repository:" )
print( f"Name: {repo_dict['name']}" )
print( f"Owner: {repo_dict['owner']['login']}" )
print( f"Stars: {repo_dict['stargazers_count']}" )
print( f"Repository: {repo_dict['html_url']}" )
print( f"Created: {repo_dict['created_at']}" )
print( f"Updated: {repo_dict['updated_at']}" )
print( f"Description: {repo_dict['description']}" )

.... end of depreciated code. """

# Terminal and File output of returned repository information.
unicode_message = "Can't print Unicode string as text."

cwd  = Path.cwd()
path = cwd / 'repos.out' 
fhandle = open( path, "w" )    # Open the file, overwriting if it exists.

header = "\nSelected information about each returned "
header += language + " repository:\n"
fhandle.write( header )
#print( header )

for repo_dict in repo_dicts:
    string = f"\nName: {repo_dict['name']}"
    #print( string )
    fhandle.write( string + "\n")


    string = f"Owner: {repo_dict['owner']['login']}"
    #print( string )
    fhandle.write( string + "\n" )

    string = f"Stars: {repo_dict['stargazers_count']}"
    #print( string )
    fhandle.write( string + "\n" )

    string = f"Repository: {repo_dict['html_url']}"
    #print( string )
    fhandle.write( string  + "\n")
    
    string = f"Description: {repo_dict['description']}"
    #print( string )
    try:
        fhandle.write( string + "\n" )
    except:
        fhandle.write( unicode_message + "\n" )

fhandle.close()

# Setup for visualization of the repo data.
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # Turn the repo name into an HTML link
    repo_name = repo_dict['name']
    repo_url  = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    #repo_link = repo_name
    repo_links.append( repo_link )
    stars.append( repo_dict['stargazers_count'] )

    # Construct the 'hover text' for each project (bar on barchart).
    owner       = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text  = f"{owner}<br />{description}"
    hover_texts.append( hover_text) 

# Make the visualization.
title  = "    Most starred " + language + " Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars' }
fig    = px.bar( x=repo_links, y=stars, title=title, labels=labels,
                 hover_name=hover_texts )
fig.update_layout( title_font_size=28, xaxis_title_font_size=20,
                   yaxis_title_font_size=20 )
fig.update_traces( marker_color='SteelBlue', marker_opacity=0.8 )
fig.show()

