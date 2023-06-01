import requests
import pandas as pd

# Assigning the URls needed to variables
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

# Making a function that is used as the main request function to get the data. This function will return the JSON data. 
def main_request(baseurl, endpoint, pageNumber):
    r = requests.get(baseurl + endpoint + f'?page={pageNumber}')
    return r.json()

# Making a function to get the number of pages in the request made. 
def get_pages(response):
    pages = response['info']['pages']
    return pages

# Making a function to get the useful information to us, which in this case is the name of each character in the series and the episodes they are in.
def parse_json(response):
    characterList = []
    for item in response['results']:
        # Adding the data we want ot a dictionary, and this dictionary will then be added to the character list created above.
        char = {
            'ID' : item['id'],
            'Character Name' : item['name'],
            'Number of Episodes' : len(item['episode']),
        }
        characterList.append(char)
    return characterList

mainList = []
data = main_request(baseurl, endpoint, 1)
for pageNumber in range(1, get_pages(data)+1):
    mainList.extend(parse_json(main_request(baseurl, endpoint, pageNumber)))

# Adding the data to a panad dataframe and saving the dataframe in a CSV file.
df = pd.DataFrame(mainList)
df.to_csv('./CharacterWithEpisodes.csv', index=False)