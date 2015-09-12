from astroid import MANAGER
from astroid import scoped_nodes

NDB_PROPERTIES = [
    'DateTimeProperty',
    'StringProperty',
    'KeyProperty',
    'StructuredProperty'
]


def register(linter):
    pass


def transform(modu):
    if modu.name == 'google.appengine.ext.ndb':
        for f in NDB_PROPERTIES:
            modu.locals[f] = [scoped_nodes.Class(f, None)]

MANAGER.register_transform(scoped_nodes.Module, transform)
