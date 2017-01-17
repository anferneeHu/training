'''entry.py'''
import sys
import proc.st_base
import proc.st_hist
import proc.st_data
from cmn.cmn_pt import pt_err

TAG_BASE = 'base'
TAG_HIST = 'hist'
TAG_CST = 'cst'


def entry(tags, code = None):
    '''entry'''
    tags = str(tags).lower()
    if tags == TAG_BASE:
        proc.st_base.test()
    elif tags == TAG_HIST:
        proc.st_hist.test_all(code)
    elif tags == TAG_CST:
        proc.st_data.test(code)
    else:
        pt_err("unknown tags:", tags)
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) == 2:
        entry(sys.argv[1])
    elif len(sys.argv) >= 3:
        entry(sys.argv[1], sys.argv[2])
    else:
        pt_err("USAGE python entry <tags>")
