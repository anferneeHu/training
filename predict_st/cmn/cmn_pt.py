'''cmn_pt'''
#import os
#import sys


def pt_err(*args):
    '''pt_err'''
    print '[E]',
    for s in args:
        print s,
    print ''


def pt_inf(*args):
    '''pt_inf'''
    print '[I]',
    for s in args:
        print s,
    print ''
