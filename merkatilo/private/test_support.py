
__all__ = [ 'TEST_SERIES_OBS', 'EMA_3_OBS', 'MA_3_OBS',
            'MO_3_OBS', 'MO_DAYS_200_OBS', 'approx', 'BENCHMARK_OBS',
            'EQUITYLINE_EMA_10_OBS', 'REVERSALS_95_105' ]

def load_test_obs(name):
    fname = '/tmp/merkatilo-test-data/{}.txt'.format(name)
    lines = [ line for line in open(fname) if not line.startswith("#") ]
    return [ (a,float(b)) for (a,b) in [ tuple(line.split()) for line in lines ]]


BENCHMARK_OBS         = load_test_obs('benchmark')
AAA_SERIES_OBS        = load_test_obs('aaa')
BBB_SERIES_OBS        = load_test_obs('bbb')
TEST_SERIES_OBS       = load_test_obs('test-series')
EMA_3_OBS             = load_test_obs('ema-3')
MA_3_OBS              = load_test_obs('ma-3')
MO_3_OBS              = load_test_obs('mo-3')
MO_DAYS_200_OBS       = load_test_obs('mo-days-200')
CROSS_EMA_30_OBS      = load_test_obs('cross-ema-30')
MO_5_CONVICTION_4_OBS = load_test_obs('mo-5-conviction-4')
EQUITYLINE_EMA_10_OBS = load_test_obs('equityline-ema-10')
REVERSALS_95_105_OBS  = load_test_obs('reversals-95-105')

def approx(n):
    big = 1000000000
    return (round(big * n) / big) if n else n
