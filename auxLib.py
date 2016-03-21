__author__ = 'james'

import numpy as np
import platform
import pickle


# ---------------- Libraries -----------------------

def elementCheck(list,e):

    x = np.array(list)
    for i in range(x.size):
        if e == x[i]:
            return True
    return False

def tupleCheck(list,e):

    for i in range(len(list)):
        if e == list[i]:
            return True
    return False

def getOS():

    o = platform.system()
    if o == "Linux":
        d = platform.dist()
        if d[0] == "debian":
            return "ubuntu"
        if d[0] == "centos":
            return "centos"
    if o == "Darwin":
        return "mac"

def loadDataStr(x):
    file2 = open(x+'.pkl', 'rb')
    ds = pickle.load(file2)
    file2.close()
    return ds

def dumpDataStr(x,obj):
    afile = open(x+'.pkl', 'wb')
    pickle.dump(obj, afile)
    afile.close()
