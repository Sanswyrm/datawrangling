# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:42:55 2020

@author: thema
"""

import xml.etree.cElementTree as ET
import pprint
import re
"""
Find the number of users that contributed to this dataset
"""

def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
       if "uid" in element.attrib:
           users.add(element.attrib["uid"])

    return users


def test():

    users = process_map('map.txt')
    pprint.pprint(len(users))
  



if __name__ == "__main__":
    test()