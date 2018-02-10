
__all__ = [ 'ema' ]

import core
from private.abbreviate import abbreviate


def ema(s, N, dates=None):
    dates = dates or core.current_dates()
    fd,ld = s.first_date(),s.last_date()
    outv = [ None for dt in range(fd,ld+1) ]
    fraction = 2/(N+1)
    remainder = 1 - fraction
    prev = None
    f = s.f
    for dt in dates:
        val = f(dt)
        newVal = (fraction * val + remainder * prev) if (core.is_valid_num(prev) and core.is_valid_num(val)) else val
        outv[dt - fd] = newVal
        prev = newVal
    return core.vector_series(outv, fd, name="EMA({},{})".format(abbreviate(s),N))



#=================================

import unittest

import obs_series
from private.test_support import TEST_SERIES_OBS, EMA_3_OBS


class EMATest(unittest.TestCase):

    def test_ema_3(self):
        TEST_SERIES = obs_series.obs_to_series(TEST_SERIES_OBS)
        EMA_3_SERIES = obs_series.obs_to_series(EMA_3_OBS)
        core.current_dates(core.dates(TEST_SERIES))
        f1 = EMA_3_SERIES.f
        f2 = ema(TEST_SERIES,3).f
        for dt in core.current_dates():
            self.assertEqual(f1(dt),f2(dt))

