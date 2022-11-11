#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 07:44:53 2022
Modified on Mo Nov 11 08:14:00 2022
@author: robert@trypuz.pl
"""
            
import os
from rdflib import Graph
import argparse

def hygiene_test(PATH_TO_FOLDER_WITH_RTS_TTLS, PATH_TO_HYGIENE_FOLDER):
    print("Gluing ontologies:")
    rts = Graph()
    for root, dirs, files in os.walk(PATH_TO_FOLDER_WITH_RTS_TTLS):
        for file in files:
            if file.endswith(".ttl"):
                print("- "+file)    
                rts_partial = Graph()
                rts_partial.parse(os.path.join(root, file), format='turtle')
                rts += rts_partial
    
    print("Hygiene checking.")
    hygiene_info = []          
    for filename in os.listdir(PATH_TO_HYGIENE_FOLDER):
        if filename.endswith(".sparql"):
            hygiene_query = open(os.path.join(PATH_TO_HYGIENE_FOLDER, filename), 'r').read()
            qres = rts.query(hygiene_query)
            hygiene_info += list(qres)
    
    hygiene_info.sort()
    for row in hygiene_info:
        print(row)
                
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in", required=True, help="path to the top folder with all turtle files")
    ap.add_argument("-t", "--tests", required=True, help="path to the folder with hygiene tests")    
    args = vars(ap.parse_args())
    hygiene_test(args["in"], args["tests"])