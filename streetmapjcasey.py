# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:30:02 2020

@author: thema
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("portland.osm.pbf","r")

#street_type.re = re.compile(r'\S+\.?, re.IGNORECASE)
street_types = defaultdict(int)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square"
            ,"Lane", "Road", "Trail", "Parkway", "Commons"]

mapping = {"St": "Street",
           "St.": "Street",
           "Ave": "Avenue",
           "Ave.": "Avenue",
           "Ct": "Court",
           "Ct.": "Court",
           "Blvd": "Boulevard",
           "Blvd.": "Boulevard",
           "Dr": "Drive",
           "Dr.": "Drive",
           "Pkwy": "Parkway",
           "Pkwy.": "Parkway",
           "Rd": "Road",
           "Rd.": "Road",
           "Ln": "Lane",
           "Ln.": "Lane"}

def audit_street_type(street_types, street_name):
    m=street_type_re.search(street_name)
    if m:
        street_type = m.group()
        street_types +=1
            
def print_sored_dict(d):
    keys = d.keys()
    keys = sorted(keys, key = lambda s:s.lower())
    for k in keys:
        v=d[k]
        print ("%s : %d" %(k,v))
        
def is_street_name(elem):
    return (elem.tag == 'tag') and (elem.attrib['k']) == "addr: street"

def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_street_name(elem):
            audit_street_type(street_types, elem.attrib['v']
        #print (sorted_dict(street_types))
        
#if __name_ '__main__'

#counts the number of tags in the file

def count_tags(filename):
    tags = {}
    
    for event, elem in ET.interparse(filename):
        if elem.tag not in tags:
            tags[elem.tag] = 1
        else:
            tags[elem.tag] +=1
return tags

#audit OSM file and change Variable mapping
    
def audit_ways ():
    for event, elem in ET.iterparse(osm_file,events=("start",)):
        if elem.tag == 'way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.abbrib['v'])
    pprint.pprint(dict(street_types))
    
#counts tag types
    
def key_type(element, keys):
    if element.tage == "tag":
        if lower.search(element.attrib['k']):
            keys['lower'] +=1
        elif lower_colon.search(element.attrib['k']):
            keys['lower_colon'] +=1
        elif problemchars.search(element.attrib['k']):
            keys['problemchars'] +=1
        else:
            keys['other'] +=1
                
#Determine the number of unique contributors
                
def get_user(element):
    return

def process_map(filename):
    users = set ()
    for __, element in ET.iterparse(filename):
        if "uid" in element.attrib:
            users.add(element.attrib["uid"])
    return users

#change street types
def update_name(name, mapping):
    m = street_type_re.search(name)
    if m:
        street+type = m.group()
        if street_type not in expected:
            name = re.sub(street_type_re, mapping[street_type], name)
return name

    

                
                
            