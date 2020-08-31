'''
functions for deriving powerCurve from original data
'''

def make_powerCurve(df_in):
    '''
    derive powerCurve from df by sorting P over v_wind
    '''
    df = df_in.copy()
    Pcol = # name of column with power-values
    df = df.groupby(Pcol).mean()
    df = df.sort_vales(by=Pcol)

    return

def logWindProf():
    '''
    apply logarithmic wind profile for different heights of data and considered case

    from .../data/log_wind_profile.py
    '''
    # define parameters for log wind profile
    zc = 10 # current height
    zt = 2 # target height
    z0 = 0.005 # surface roughness in m (source: https://en.wikipedia.org/wiki/Roughness_length)
    u_zc = df.vW # current wind velocity from data

    # determine wind velocity at target height zt using rearranged log wind profile
    u_zt = u_zc*(np.log(zt/z0)/np.log(zc/z0))
    return


def fit_pC():
    '''
    use curveFitting method to derive valid powerCurve from dataset
    '''

    fitfun = pC_curveFit(x0 , y0)
    new_y = fitfun(new_x)

    return

def pC_curveFit(x_in, y_in):
    '''
    from .../curve_fit/make_powerCurve_v01.py
    '''
    x = np.array(x_in)
    y = np.array(y_in)
    z = np.polyfit(x, y, 75)
    p = np.poly1d(z)
    return p
