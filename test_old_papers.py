#!/usr/bin/env python

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://lod.kb.nl/sparql")
sparql.setQuery("""
PREFIX dc: <http://purl.org/dc/elements/1.1/>
SELECT ?s, ?o, ?p
WHERE {
 ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Article>.
 ?s dc:identifier ?o.
 ?s <http://lod.kb.nl/ontology/ocr> ?p.
} LIMIT 10
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

records = []
for result in results["results"]["bindings"]:
    fields = {
        's': 'id',
        'o': 'link',
        'p': 'ocr'
    }
    record = {}
    for fld in fields.keys():
      record[fields[fld]] = result[fld]['value']
    records.append(record)
print(records)
