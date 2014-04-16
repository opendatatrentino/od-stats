#!/usr/bin/env python

from __future__ import print_function, division

import os
import json
import jinja2

from utils import load_configuration

here = os.path.abspath(os.path.dirname(__file__))


def main():
    conf = load_configuration('conf.ini')

    with open(os.path.join(here, 'data', 'counters.json')) as fp:
        counters_data = json.load(fp)

    counters = []
    sortkey = lambda x: counters_data[x[0]]
    cconf = sorted(conf['catalogs'].iteritems(), key=sortkey, reverse=True)
    maxcount = max(counters_data.itervalues())

    for name, catalog in cconf:
        count = counters_data[name]
        counters.append({
            'name': name,
            'title': catalog.get('title') or name,
            'cfg': catalog,
            'count': count,
            'width': '{0:.2f}'.format(count * 100 / maxcount),
        })

    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    env = jinja2.Environment(loader=loader)
    template = env.get_template('index.jinja')
    rendered = template.render({
        'counters': counters,
    })

    print(rendered)


if __name__ == '__main__':
    main()
