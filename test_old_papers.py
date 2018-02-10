#!/usr/bin/env python

from time import sleep
import shutil
import hashlib
import json

from SPARQLWrapper import SPARQLWrapper, JSON
import requests

sparql = SPARQLWrapper("http://lod.kb.nl/sparql")
sparql.setQuery("""
PREFIX dc: <http://purl.org/dc/elements/1.1/>
SELECT ?s, ?o, ?p
WHERE {
graph <http://lod.kb.nl/kranten/> {
 ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Article>.
 ?s dc:identifier ?o.
 ?s <http://lod.kb.nl/ontology/ocr> ?p.
}
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

    r = requests.get(record['ocr'], stream=True)
    path = './ocr/%s.xml' % (hashlib.sha224(record['id']).hexdigest(),)
    record['file'] = path
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    sleep(1)
    records.append(record)
print json.dumps(records)
