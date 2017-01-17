'''st_data.py'''
import pandas as pd
from cmn.cmn_tag import *
from cmn.cmn_pt import *
from cmn.cmn_save import *


class CST(object):
    '''st class'''

    def __init__(self, code):
        self.code = code
        self.data = None

    def get_data(self):
        self.data = cmn_load(self.code)

    def pt(self):
        pt_inf("code", self.code)
        pt_inf("data", self.data)


def test(code = None):
    if code is None or code=="":
        code = '600000'
    cst = CST(code)
    cst.get_data()
    cst.pt()
