'''st_base.py'''
#import os
#import sys
#import pickle
import tushare as ts
from cmn.cmn_save import cmn_save
from cmn.cmn_pt import pt_inf
from cmn.cmn_tag import ST_BASE_FILE

# pt_inf(ts.__version__)


def get_base(filename=ST_BASE_FILE):
    '''get_base'''
    st_lst = ts.get_stock_basics()
    pt_inf(st_lst.index)
    cmn_save(st_lst, filename)
    # st_lst.to_csv('st_base.csv')


def test():
    '''test'''
    get_base()

if __name__ == "__main__":
    get_base()
