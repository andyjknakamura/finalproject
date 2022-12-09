from xml.sax import parseString
import re
from bs4 import BeautifulSoup
import requests
import os
import csv
import unittest
import sqlite3
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': "f625e8875cad4052bc9e29872bd62523",
    'client_secret': "c145b321c26b42e1871b412a8eeb48e7",
    })

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
print(access_token)


headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/artists/'
ID = "0TnOYISbd1XYRBk9myaseg"
r = requests.get(BASE_URL + ID, headers=headers)
r = r.json()
print(r)
