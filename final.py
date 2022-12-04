#AJ Group
#Jess Yang, Andrew Nakamura
#SI 206 Final Project
from xml.sax import parseString
from bs4 import BeautifulSoup
import re
import requests
import os
import csv
import unittest
import sqlite3

def open_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#def maps_database:
#   Jess
#   Creating the database from the maps API with 
#   categories such as city name, # of supermarkets

def cities_database(link, cur, conn):
#   Andrew
#   Creating the database from urls with
#   categories such as city name, median household income level, racial demographics of the area,
#   income change over time(?)
    resp = requests.get(link)
    soup = BeautifulSoup(resp.content, 'html.parser')
    td_list = soup.find_all('td')
    tup_list = []
    for i in range(5, len(td_list), 3):
        split_data = td_list[i+2].text.split(' / ')
        city_name = re.findall('([A-Za-z\s]*), MI', split_data[0])
        tup = (city_name[0], split_data[1], td_list[i+1].text)
        tup_list.append(tup)
    print(tup_list)
    cur.execute("DROP TABLE IF EXISTS Cities")
    cur.execute("CREATE TABLE Cities (name TEXT, population TEXT, income TEXT)")
    for item in tup_list:
        cur.execute("INSERT INTO Cities (name, population, income) VALUES (?, ?, ?)", item)
    conn.commit()

#def restaurant_ratio:
#   Jess
#   Calculating ratio of fast food restaurants to total restaurants in the area

#def income_calc:
#   Andrew
#   Not sure about this one quite yet tbh

class TestCases(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    #more code here
    cur, conn = open_database('project.db')
    cities_database('http://www.usa.com/rank/michigan-state--median-household-income--city-rank.htm?hl=&hlst=&wist=&yr=9000&dis=&sb=DESC&plow=&phigh=&ps=', cur, conn)
    unittest.main(verbosity=2)