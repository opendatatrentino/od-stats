#!/usr/bin/env python

import os
import json

import requests

from utils import load_configuration

here = os.path.abspath(os.path.dirname(__file__))


def count_ckan_datasets(catalog):
    if 'list_url' in catalog:
        list_url = catalog['list_url']
    else:
        list_url = catalog['url'] + '/api/2/rest/dataset'
    resp = requests.get(list_url)
    return len(resp.json())


def count_datasets_opendataground_it(catalog):
    url = ('http://dati.opendataground.it/browse?organization={0}'
           '&q=&df=contents&start=0&rows=0&output=json'
           .format(catalog['organization']))
    resp = requests.get(url)
    return int(resp.json()['totalDocs'])


def count_datasets(catalog):
    if catalog['type'] == 'ckan':
        return count_ckan_datasets(catalog)
    if catalog['type'] == 'opendataground_it':
        return count_datasets_opendataground_it(catalog)
    raise ValueError("Unsupported catalog type: {0}".format(catalog['type']))


def main():
    # We want to update counters for each catalog
    # and print on the standard output.
    counters = {}

    conf = load_configuration('conf.ini')
    for catalog_name, catalog in conf['catalogs'].iteritems():
        counters[catalog_name] = count_datasets(catalog)

    print(json.dumps(counters))


if __name__ == '__main__':
    main()
