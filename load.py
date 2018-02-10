
__all__ = [ 'lo' ]

import core, obs_series, os

def lo(name):
    fname = '{}/TIME_SERIES/{}/CLOSE'.format(os.getenv('HOME'),name)
    entries = []
    with open(fname) as f:
        for line in f:
            try:
                pair = line.split()
                entries.append((core.to_jdate(pair[0]),float(pair[1])))
            except:
                pass
    return obs_series.obs_to_series(entries, name=name)


