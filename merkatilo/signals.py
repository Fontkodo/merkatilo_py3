
__all__ = [ 'to_signals' ]

import merkatilo.core as core
from merkatilo.private.utils import signalify_vector_copy
from merkatilo.private.abbreviate import abbreviate

def to_signals(s, dates=None):

    '''Transform a series into non-repeating negative-one (-1) where the input is negative
       non-repeating one (1) where the input is non-negative.'''
    
    dates = dates or core.current_dates()
    vals = list(map(s.f, dates.vec))
    sigv = signalify_vector_copy(vals)

    fd = dates.first_date()
    ld = dates.last_date()
    outv = [ None for dt in range(fd,ld+1) ]

    for (dt,sig) in zip(dates,sigv):
        if sig:
            outv[dt - fd] = sig

    return core.vector_series(outv, fd, name='sigs({})'.format(abbreviate(s)))
