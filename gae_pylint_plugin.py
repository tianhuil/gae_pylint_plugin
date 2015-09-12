from astroid import MANAGER
from astroid import scoped_nodes

# list from https://cloud.google.com/appengine/docs/python/ndb/properties
NDB_PROPERTIES = [
    'IntegerProperty',
    'FloatProperty',
    'BooleanProperty',
    'StringProperty',
    'TextProperty',
    'BlobProperty',
    'DateTimeProperty',
    'DateProperty',
    'TimeProperty',
    'GeoPtProperty',
    'KeyProperty',
    'BlobKeyProperty',
    'UserProperty',
    'StructuredProperty',
    'LocalStructuredProperty',
    'JsonProperty',
    'PickleProperty',
    'GenericProperty',
    'ComputedProperty',
]


def register(linter):
    pass


def transform(modu):
    if modu.name == 'google.appengine.ext.ndb':
        for f in NDB_PROPERTIES:
            modu.locals[f] = [scoped_nodes.Class(f, None)]

MANAGER.register_transform(scoped_nodes.Module, transform)
