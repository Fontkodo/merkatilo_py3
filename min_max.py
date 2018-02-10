
__all__ = [ 'min_max_obs', 'max_ob', 'min_ob' ]

import core

def min_max_obs(s, dates=None):
    dates = dates or core.current_dates()
    min_ob = None
    max_ob = None
    f = s.f

    for dt in dates:
        val = f(dt)
        if core.is_valid_num(val):
            if not min_ob:
                min_ob = max_ob = (dt,val)
            if min_ob[1] > val:
                min_ob = (dt,val)
            if max_ob[1] < val:
                max_ob = (dt,val)

    return min_ob, max_ob

def min_ob(s, dates=None):
    return min_max_obs(s,dates=dates)[0]

def max_ob(s, dates=None):
    return min_max_obs(s,dates=dates)[1]




#===================================

import unittest
from private.test_support import TEST_SERIES_OBS
from obs_series import obs_to_series

class MinMaxTests(unittest.TestCase):

    def setUp(self):
        self.TEST_SERIES = obs_to_series(TEST_SERIES_OBS)
        core.current_dates(core.dates(self.TEST_SERIES))

    def testMin(self):
        ob = min_ob(self.TEST_SERIES)
        self.assertEqual(ob[0], core.to_jdate('2012-1-13'))
        
    def testMax(self):
        ob = max_ob(self.TEST_SERIES)
        self.assertEqual(ob[0], core.to_jdate('2014-9-18'))
        
        
        
