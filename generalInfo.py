import requests

# Assigning the URls needed to variables
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

# Making the request
r = requests.get(baseurl + endpoint)

# You print this out to see the response you get. 
# 404 means that the page doesn't exist. 
print(r)

# We don't want the response above, we want the json response.
data = r.json()

# You can now access the data just the way you did in a dictionary using square brackets
print(data['info'])

# To get the number of pages from the info field. This format can be used to pick out any information.
# You are basically accessing different parts of the JSON data.
pages = data['info']['pages']
name = data['results'][0]['name']
episodes = data['results'][0]['episode']

# If we want to know the number of episodes, we should simply get the length of the episode list. 
print(len(episodes))


