# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:15:58 2020

@author: thema
"""

###Parse the file for Bartlett, TN 'map.txt' and create a dictionary for each tag

import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    tree=ET.iterparse(filename)
    tags={}
    for event,elem in tree:
        if elem.tag not in tags.keys():
            tags[elem.tag]=1
        else:
            tags[elem.tag] = tags[elem.tag]+1
    return tags    
def test():

    tags = count_tags('map.txt')
    pprint.pprint(tags)
    #assert tags == {}

    

if __name__ == "__main__":
    test()