from astroid import MANAGER
from astroid import scoped_nodes
from google.appengine.api import memcache
from google.appengine.ext import ndb

def register(linter):
    pass

def transform(modu):
    if modu.name == 'google.appengine.ext.ndb':
        for f in [f for f in ndb.__dict__.keys() if 'Property' in f]:
            modu.locals[f] = [scoped_nodes.Class(f, None)]

    if modu.name == 'google.appengine.api.memcache':
        for f in memcache.__dict__.keys():
            modu.locals[f] = [scoped_nodes.Class(f, None)]

MANAGER.register_transform(scoped_nodes.Module, transform)
