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
import spotipy.util as util

"""username = 'Jess'
scope = 'user-library-read'
util.prompt_for_user_token(username,scope,client_id='f625e8875cad4052bc9e29872bd62523',client_secret='c145b321c26b42e1871b412a8eeb48e7',redirect_uri='http://localhost/')
# token 你的token，在运行上面的代码后，会显示在http://localhost/里面"""
token='BQDw9RBvTvDrwIU2pYEqUHFaL'
headers = {"Authorization": "Bearer {}".format(token)}
parms = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
response = requests.get("https://api.spotify.com/v1/artists", parms, headers= headers)
data = response.text
in_list = json.loads(data)
print(in_list)