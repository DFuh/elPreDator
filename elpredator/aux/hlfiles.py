#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:37:55 2020

@author: dafu_res
"""


'''
functions for handling files
'''
import os
import glob
from collections import defaultdict

### return list of files in directory; optional: based on keywords

def mk_fllst(pth, flnm = None, fltr_files=False, raw=False):
        '''make file list...
        filter by multiple keys
        '''
        if not flnm:
            flpth = pth
        else:
            flpth = pth+'/'+flnm
        ### loop for sorting files
        print(' --- read files --- ')
        fllst0 = glob.glob(flpth + '/*.csv')#, recursive=True)
        print('Files in directory: ')
        for fl in fllst0:
            print(fl)

        fltr = False
        if not fltr_files:
            if input('Filter by keyword? [y/n]').lower()=='y':
                fltr = True
        else:
            fltr = True

        if fltr:
            fllst0 = filter_by_keywords(fllst0)

        #TODO: plant_list = self.extract_plantID(_fl)

        #fltrd_lst.sort() # = sorted(self.fllst)
        if not raw:
            print(' --- sort list alphabetically --- ')
            fllst0.sort() # basic sorting func.; alphabetical
        #self.fllst = fltrd_lst
        return fllst0


def filter_by_keywords(fllst):
    k=0
    l = ['1st','2nd','3rd']
    fltr=True
    while fltr:

        if k <2:
            strng1 = l[k]
        else:
            strng1 = str(k)+'th'
        kw = input('Enter'+strng1+'keyword:')
        print('Files in list: \n')
        fllst1 = []
        for _fl in fllst:
            if kw in _fl:
                fllst1.append(class dataInstance():

    def __init__():
        pass_fl)
                print(_fl+'\n')
        #fllst0 = fllst1.copy()
        fltr= input('Do you want to filter by another keyword? [y/n]').lower()=='y'

    return fllst1

def find_plant_name(flnm_raw, splitdelim="_"):
    '''
    read first filename and find plant-name
    (apply to following files)
    '''

    flnm0, ftype = os.path.splitext(flnm_raw)
    bnm = os.path.basename(flnm0)
    dirnm = os.path.dirname(flnm0)
    if not input(f'Split by {splitdelim} ? [y/n]').lower()=='y':
        splitdelim = input('Enter delimiter to split by: ')

    prnt = f'Basename: {bnm} contains {bnm.split(splitdelim)}'
    print(prnt)
    ec = False # entered correctly
    while not ec:
        locplntnm = input('Which one is the plantID? [Enter int]')
        try:
            plntnm_idx = int(locplntnm)
            ec = True
        except:
            pass
    plntID = bnm.split(splitdelim)[plntnm_idx]
    print('Choosen plantID: {}'.format(plntID))
    use for all????
    return


def group_by_plant( flnm_specs): #TODO: details of flnm_specs
        ''' create dict with basic infos out of path-string
        group by plant id
        '''
        #TODO: optional list keys and order of keys
        ## ver1: plantID_name_dateStart?dateEnd
        ## ver2: plantID_dateStart?dateEnd
        ## ver3: plantID_dateStart?dateEnd_name

        print('...group files...')
        #directory = self.pth + str(yr_in)+'/'
        #print('dir:',directory)
        #s_files = read_files() #Read all files in given path
        print('filelist:',s_files)
        groups = defaultdict(list)

        #for filename in os.listdir(directory):

        for filename in s_files:
            basename, extension = os.path.splitext(filename)
            bn2 = os.path.basename(filename) # Extract filename from whole path-name
            #print('bn:',basename)
            #print('bn2:',bn2)
            try:
                # TODO: what, if no "nm" in filename? -> set in options
                plant, nm, date = bn2.split('_') # split filename in plant_name, ..., start-date, end-date
            except:
                plant, nm, start, end = bn2.split('_') # split filename in plant_name, ..., start-date, end-date

            groups[plant].append([filename,start[3:],end[:-4]])

        for plnt in groups:#.keys():
            groups[str(plnt)].sort()

        return groups
