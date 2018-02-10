__all__ = [ 'conviction' ]

import core
from private.utils import signalify_vector_copy

def conviction(s, N, dates=None):
    
    '''A conviction signal series avoids signal whipsaws by forcing signals to
    persist N periods before firing.  The signal, if fired, is delayed by N periods
    as well.  For instance, with a conviction of 1, two sequential signals are 
    simply erased.  If not erased, the signal values of the input are delayed by 
    one period.'''
    
    dates = dates or core.current_dates()
    dv = [ dt for dt in dates ]
    vals = list(map(s.f, dates))
    sigv = signalify_vector_copy(vals)

    last_ndx = -1000000
    for (ndx,sig) in enumerate(sigv):
        if sig:
            if (ndx - last_ndx <= N):
                sigv[ndx] = None
                sigv[last_ndx] = None
            last_ndx = ndx

    fd = dates.first_date()
    ld = dates.last_date()
    outv = [ None for dt in range(fd,ld+1) ]

    for (sig,dt) in zip(sigv,dv[N:]):
        if sig:
            outv[dt - fd] = sig

    return core.vector_series(outv, fd)





#===============================================
from common_testing_base import CommonTestingBase, obs_to_series
from momentum import mo

from private.test_support import MO_5_CONVICTION_4_OBS

class ConvictionTest(CommonTestingBase):

    def test_ema_3(self):
        MO_5_CONVICTION_4_SERIES = obs_to_series(MO_5_CONVICTION_4_OBS)
        f1 = MO_5_CONVICTION_4_SERIES.f
        f2 = conviction(mo(self.TEST_SERIES,5),4).f
        for dt in core.current_dates():
            self.assertEqual(f1(dt),f2(dt))

