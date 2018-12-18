__version__ = '0.0.0'
__authors__ = 'Dariusz Izak IBB PAS'

__all__ = [
    'pubot',
]

try:
    import scholarly as _sch
except ImportError:
    print('Could not import dependencies. Ignore if running setup.')
