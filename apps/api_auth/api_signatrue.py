#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time     : 2020/12/3
# Author   : DemonCaptain
# FileName : apiSignature.py

# here put the import lib

import hashlib
import random
import sys
import time
# import config

class apiSignature:

    def __init__(self,uri):
        self.ak = "chuangkey2019"
        self.ts = 600
        self.uri = uri

    def computeSignature(self):
        # print(self.uri, "\n", self.ak, "\n", self.ts)
        timestamp = str(int(time.time()) + int(self.ts))
        rand = str(random.randint(1, sys.maxsize))
        m = hashlib.md5()
        m.update(("%s-%s-%s-%s" % (self.uri, timestamp, rand, self.ak)).encode("utf-8"))
        token = "%s-%s-%s" % (timestamp, rand, m.hexdigest())
        return token


if __name__ == '__main__':
    path =  '/admin/rdata/'
    ini_sigin = apiSignature(uri=path)
    sigin = ini_sigin.computeSignature()
    print(sigin)