import requests

url = 'https://static.tildacdn.com/tild3338-3936-4966-b936-663163356536/photo.ico'

r = requests.get(url)
with open('skill.ico', 'wb') as f:
    f.write(r.content)