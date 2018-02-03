registry = {}
from types import SimpleNamespace as ns

class metameta(type):
    '''Getattr on effect should return the namespace'''

    def __getattr__(cls, name):
        print(name)
        print(registry)
        if name in registry:
            return registry[name]
        else:
            return None


class effect(type, metaclass=metameta):
    def __new__(meta, name, bases, dct):
        eff = {}
        eff['setup'] = dct['setup']
        eff['action'] = dct['action']

        registry[name] = ns(**eff)
        return None


from . import *
