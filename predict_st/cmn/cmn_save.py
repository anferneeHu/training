'''cmn_save.py'''
#import sys
import os
import pickle
import pandas as pd
from cmn_tag import *
from cmn_pt import *


def pkl_save(data, filename):
    '''pkl_save'''
    with open(filename, 'w') as f:
        pickle.dump(data, f)
    return True


def pkl_load(filename):
    '''pkl_load'''
    data = None
    with open(filename, 'r') as f:
        data = pickle.load(f)
    return data


def csv_save(data, savename):
    '''csv_save'''
    return data.to_csv(savename)


def csv_load(savename):
    '''csv_load'''
    return pd.read_csv(savename)


def cmn_save(data, savename, save_path=G_DEFAULT_PATH, save_type=G_DEFAULT_SAVE_TYPE):
    '''cmn_save'''
    if save_type == 'csv':
        filename = os.path.abspath(os.path.join(
            save_path, savename + CSV_SUFFIX))
        return csv_save(data, filename)
    else:
        filename = os.path.abspath(os.path.join(
            save_path, savename + PKL_SUFFIX))
        return pkl_save(data, filename)


def cmn_load(savename, save_path=G_DEFAULT_PATH, save_type=G_DEFAULT_SAVE_TYPE):
    '''cmn_load'''
    if save_type == 'csv':
        filename = os.path.abspath(os.path.join(
            save_path, savename + CSV_SUFFIX))
    else:
        filename = os.path.abspath(os.path.join(
            save_path, savename + PKL_SUFFIX))

    if not os.path.exists(filename):
        pt_err('Save file', filename, 'not found')
        return None
    if save_type == 'csv':
        return csv_load(filename)
    else:
        return pkl_load(filename)
