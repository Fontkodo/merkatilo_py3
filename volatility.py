

__all__ = [ 'volatility' ]

from private.standard_deviation import standard_deviation
from private.series_dates_values import series_dates_values
from momentum import mo_days

import core

def volatility (s, days=365, dates=None):

    '''volatility is the standard deviation of the mo_days calculation.'''
    
    dates = dates or core.current_dates()
    vals = series_dates_values(mo_days(s,days=days,dates=dates),dates)
    return standard_deviation(vals)


#=====================================

from common_testing_base import CommonTestingBase, approx

class test_volatility(CommonTestingBase):

    def test_volatility(self):
        v = volatility(self.TEST_SERIES, days=200)
        self.assertEqual(approx(v), approx(0.0468086666214253))
