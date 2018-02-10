#!/usr/bin/env python

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://lod.kb.nl/sparql")
sparql.setQuery("""
SELECT ?s
WHERE {
 ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Article>
} LIMIT 10
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)
