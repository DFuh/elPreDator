#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:57:18 2020

@author: dafu_res
"""


'''
functions for reading data
'''

import pandas as pd

def read_file(pth, ucols=None, cols_to_try=None):
    ''' read files from given path
    try different types of separators (, and ;)
    try different column-lists
    return df
    '''
    #TODO: set variable for avoiding recursive tests

    if cols_to_try:
        fcols = ucols.copy()
        fcols= fcols.extend(cols_to_try)
        try:
            try:
                df = pd.read_csv(pth, usecols=fcols)
            except:
                df = pd.read_csv(pth, sep=';',decimal=',', usecols=fcols)
        except:
            try:
                df = pd.read_csv(pth, usecols=ucols)
            except:
                df = pd.read_csv(pth, sep=';',decimal=',', usecols=ucols)
    else:
        try:
            df = pd.read_csv(pth)
        except:
            df = pd.read_csv(pth, sep=';',decimal=',')
    return df


def ctrl_murd(fllst):
    '''
    read and return list of multiple dataFrames
    '''
    df_list = []
    for nm in fllst:
        df = read_file(nm)
        df_list.append(df)
    return df_list


def rename_columns(df):
        ncols=[]
        #cols = df.columns
        '''
        for strng in cols: #TODO: replace by switch?
            strng = strng.replace(' ', '_')
            strng = strng.replace('Datum(Server)_Uhrzeit(Server)','Date')
            strng = strng.replace('Windgeschwindigkeit', 'v_W')
            strng = strng.replace('Leistung','P')
            ncols.append(strng)
        '''
        '''
        def sw_par(nm):
            switcher = {
                'wind_list': 'jep',
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }
            strng =  switcher.get(case, None)
            return strng
        '''
        if 'Unnamed: 0' in df.columns:
            df = df.drop(['Unnamed: 0'], axis = 1) # drop column
        cols = df.columns
        wind_list = ['vw', 'v_w','wind'] #possibkle column names for wind velocity
        pow_list = ['P', 'Leistung','power'] #possibkle column names for plant power
        dat_list = ['Datum', 'Date']
        #TODO: what about max/min ?
        w_mimx = [[],[]]
        p_mimx = [[],[]]
        w_idx = []
        p_idx = []
        new_cols = []
        w_cnt = 0
        p_cnt = 0
        dat_cnt=0
        for i,col in enumerate(cols):
            if any([ele for ele in wind_list if(ele in col)]):

                w_idx.append(i)

                if len(col.split(' '))>1:
                    if 'min' in col.lower():
                        w_mimx[0].append(i)
                        new_cols.append('vW_'+str(w_cnt)+'_min')
                    elif 'max' in col.lower():
                        w_mimx[1].append(i)
                        new_cols.append('vW_'+str(w_cnt)+'_max')
                else:
                    w_cnt+=1
                    new_cols.append('vW_'+str(w_cnt)+'_')

            elif any([ele for ele in pow_list if(ele in col)]):
                p_idx.append(i)

                if len(col.split(' '))>1:
                    if 'min' in col.lower():
                        p_mimx[0].append(i)
                        new_cols.append('P_'+str(p_cnt)+'_min')
                    elif 'max' in col.lower():
                        p_mimx[1].append(i)
                        new_cols.append('P_'+str(p_cnt)+'_max')
                else:
                    p_cnt +=1
                    new_cols.append('P_'+str(p_cnt)+'_')

            elif any([ele for ele in dat_list if(ele in col)]):

                if dat_cnt >0:
                    strng = 'Date '+str(dat_cnt)
                else:
                    strng = 'Date'
                new_cols.append(strng)
            else:
                new_cols.append(col)
            dat_cnt +=1
        #col_arr = np.array(cols)
        #w_ele =

            #bool_answ = any(ele in col for ele in test_list)
        #TODO what, if more than one col?
            #if
        prnt_lst = [w_mimx, p_mimx, w_idx, p_idx]
        nm_lst = ['w_mimx', 'p_mimx', 'w_idx', 'p_idx']
        for i,ele in enumerate(prnt_lst):
            print(nm_lst[i]+': ', ele)
        print('old: ', cols)
        print('new cols: ', new_cols)
        #return
        df.columns = new_cols
        return df
