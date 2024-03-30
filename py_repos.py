""" A script to query GitHUB python repositories. """

import requests            # To make API calls to a website
from pathlib import Path   # For file I/O


# Setup the URL (target) for the request
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = { "Accept": "application/vnd.github.v3+json" }
r = requests.get( url, headers=headers )
print( f"Status code: {r.status_code}" )

# Convert the response object to a Python dictionary.
response_dict = r.json()

# Process the results (response).
print( response_dict.keys() )
print( f"Total repositories: {response_dict['total_count']}" )
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
fhandle = open( path, "w" )    # Open the file, overwritting if it exists.

header = "\nSelected information about each returned repository:\n"
fhandle.write( header )
print( header )

for repo_dict in repo_dicts:
    string = f"\nName: {repo_dict['name']}"
    print( string )
    fhandle.write( string + "\n")


    string = f"Owner: {repo_dict['owner']['login']}"
    print( string )
    fhandle.write( string + "\n" )

    string = f"Stars: {repo_dict['stargazers_count']}"
    print( string )
    fhandle.write( string + "\n" )

    string = f"Repository: {repo_dict['html_url']}"
    print( string )
    fhandle.write( string  + "\n")
    
    string = f"Description: {repo_dict['description']}"
    print( string )
    try:
        fhandle.write( string + "\n" )
    except:
        fhandle.write( unicode_message + "\n" )

fhandle.close()
