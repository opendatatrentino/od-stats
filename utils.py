from ConfigParser import RawConfigParser


def load_configuration(filename):
    cfp = RawConfigParser()
    cfp.read(filename)
    conf = {'catalogs': {}}

    for section in cfp.sections():
        parts = section.split(':')

        if parts[0] == 'catalog' and len(parts) == 2:
            name = parts[1]
            _catalog = {}
            for option in cfp.options(section):
                _catalog[option] = cfp.get(section, option)
            conf['catalogs'][name] = _catalog

    return conf
