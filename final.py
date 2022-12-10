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

#def maps_table:
#   Jess
#   Creating the database from the maps API with 
#   categories such as city name, # of supermarkets

def billboard_table(link, cur, conn):
#   Andrew
#   Creating the database from urls with
#   categories such as city name, median household income level, racial demographics of the area,
#   income change over time(?)
    resp = requests.get(link)
    soup = BeautifulSoup(resp.content, 'html.parser')
    n_list = []
    r_list = []
    tag = soup.find(class_="chart-results-list // u-padding-b-250")
    #print(tag)
    name_list = tag.find_all('h3')
    for item in name_list:
        name = item.text
        n_list.append(name.strip('\n\t'))
    rank_list = tag.find_all('span')
    for item in rank_list:
        rank = item.text
        r_list.append(rank.strip('\n\t'))
    tup_list = []
    for i in range(100):
        tup = (r_list[i], n_list[i])
        tup_list.append(tup)
    #print(tup_list)
    cur.execute("DROP TABLE IF EXISTS Cities")
    cur.execute("DROP TABLE IF EXISTS Charts")
    cur.execute("CREATE TABLE Charts (name TEXT, rank INTEGER)")
    for item in tup_list:
        cur.execute("INSERT INTO Charts (name, rank) VALUES (?, ?)", item)
    conn.commit()

    #print out database
    cur.execute("SELECT name,rank FROM Charts")
    for row in cur:
        print(row)
    cur.close

class TestCases(unittest.TestCase):
    def setUp(self):
        pass

if __name__ == '__main__':
    #more code here
    cur, conn = open_database('project.db')
    billboard_table('https://www.billboard.com/charts/year-end/top-artists/', cur, conn)
    unittest.main(verbosity=2)