#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 07:44:53 2022
Modified on Mo Nov 11 08:14:00 2022
@author: robert@trypuz.pl
"""
import argparse
import os
from ots_no_bnodes import OrderedTurtleSerializer
from rdflib import Graph
from rdflib.namespace import OWL


def serialize_turtle(top_folder_with_all_ttls):
    print("Normalizing:")
    for root, dirs, files in os.walk(top_folder_with_all_ttls):
        for file in files:
            if file.endswith(".ttl"):
                print("- "+file)
                rts = Graph()
                rts.parse(os.path.join(root, file), format="turtle")
                serializer = OrderedTurtleSerializer(rts)                
                serializer.class_order = [
                    OWL.Ontology,
                    OWL.Class,
                    OWL.ObjectProperty,
                    OWL.DatatypeProperty,
                    OWL.AnnotationProperty,
                    OWL.NamedIndividual
                ]
                out = open(os.path.join(root, file), 'wb')                
                serializer.serialize(out)
                out.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--tfolder", required=True, 
                    help="path to the top folder with all turtle files")
    args = vars(ap.parse_args())
    serialize_turtle(args["tfolder"])