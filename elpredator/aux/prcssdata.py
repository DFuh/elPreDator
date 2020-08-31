#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:08:08 2020

@author: dafu_res
"""
pwrCrv

'''
process the data read
- clean df
- fill gaps in date
- fill gaps in values [wind, ]
-
'''

#TODO: ensure input of df with non-ambigous column-names

def clean_df(df_in):
    '''
    clean dataFrame
    - remove non-plausible values within set limits
    - remove NaN in P

    ## yet to be implemented:
        - get PN (nominal/ rated power of plant) -> idea: average max P, round() to kW (2133.5 -> 2000)
    '''


    stridx = '' ???
    df = df_in.copy()
    df.columns = []
    df.set_index(stridx)

    ### df limits
    wind_lim = [0, 35]  # // in m/s
    P_lim = [0, 1.2*PN] # get PN ?

    for col in df.columns:
        if ('wind' in col.lower()) or ('vw' in col.lower()) or ('v_w' in col.lower()):
            lim = wind_lim
        elif ('leistung' in col.lower()) or ('P' in col):
            lim = P_lim
            df = df[df[col].notna()] # remove NaN-values in P-column

        df[col] = np.where(df[col]<=lim[0],0,df[col]) # min limit
        df[col] = np.where(df[col]<lim[1],df[col],0) # max limit

    return df


def cmpl_dates(df_in):
        '''
        complete dates (date-range)
        
        '''

        df = df_in.copy()

        df = df.rename(columns = {'Datum(Server)_Uhrzeit(Server)':'Date'})#, inplace = True)
        df['Date'] = pd.to_datetime(df['Date'])
        r = pd.date_range(start=df.Date.min(), end=df.Date.max(), freq='10min') #TODO: not always valid !!!
        #print(r)
        #print('duplicates in df:', df[df.index.duplicated()])
        #df = df.set_index('Date',inplace=True)
        print('len of dfB (1): ', len(df))
        print('duplicates in df:', df[df.index.duplicated()])

        df = df.drop_duplicates(subset='Date')

        df = df.set_index('Date')#,inplace=True)
        print(df.head())
        print('duplicates in df (ad):', df[df.index.duplicated()])
        df = df.reindex(r).rename_axis('Date')#.fillna(-100)#.rename_axis('nDate').reset_index()
        print('++++++ head: ', df.head())
        print('len of dfB (2): ', len(df))

        return df
