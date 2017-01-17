'''st_hist'''
#import os
#import sys
#import pickle
import tushare as ts
from cmn.cmn_tag import *
from cmn.cmn_save import *
from cmn.cmn_pt import *
from cmn.cmn_funcs import *


def get_hist_by_code(codes):
    '''get_hist_by_code'''
    data = ts.get_hist_data(codes)
    if data is not None:
        cmn_save(data, codes)
        return True
    return False


def get_all_hist(st_base_file=ST_BASE_FILE):
    '''get_all_hist'''
    st_base = cmn_load(st_base_file)
    if st_base is None:
        pt_err("get st base err", st_base_file)
        return False
    for codes in st_base['code']:
        codes = form_code(codes)
        pt_inf("now getting", codes, "...")
        if not get_hist_by_code(str(codes)):
            pt_err("got", codes, "err")
    pt_inf("All got.")
    return True


def test():
    '''test'''
    codes = '600000'
    get_hist_by_code(codes)


def test_all(code=None):
    '''test_all'''
    if code is None or code=='':
        get_all_hist()
    else:
        get_hist_by_code(code)

if __name__ == "__main__":
    test_all()
