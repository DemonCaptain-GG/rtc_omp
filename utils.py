#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time       : 2021/7/5
@Author     : DemonCaptain
@ScriptName : utils.py
"""

# here put the import lib
import time


def get_tim():
    time_str = time.strftime("%Y {} %m {} %d {} %X")
    return time_str.format("年", "月", "日")

if __name__ == '__main__':
    print(get_tim())