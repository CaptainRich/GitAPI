""" A script to query GitHUB python repositories. """

import requests            # To make API calls to a website

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

# Report on the first repo returned.
repo_dict = repo_dicts[0]
print( f"\nKeys: {len(repo_dict)}" ) 

for key in sorted( repo_dict.keys() ):
    print( key )