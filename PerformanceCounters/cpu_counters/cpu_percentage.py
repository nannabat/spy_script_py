from __future__ import division
import subprocess
import datetime
import json
import socket
import fcntl
import struct
import psutil
import time
import datetime
import collections
import os

def get_proc():
    number = subprocess.check_output("cat /proc/cpuinfo | grep processor", shell=True)
    return number
cpunumber = get_proc()


def get_allcpu():
    ts_return_list = []
    value = psutil.cpu_percent(percpu=True)
    ts_time_stamp = time.time()
    ts_st = datetime.datetime.fromtimestamp(ts_time_stamp).strftime('%Y-%m-%d %H:%M:%S') 
    ts_return_list.append(value)
    ts_return_list.append(ts_st)
    return ts_return_list
value = get_allcpu()

list = []
for i in range(1,6):
     time.sleep(5)
     list.append(get_allcpu())   

cpu0 = [[list[0][0][0], list[0][1]], [list[1][0][0], list[1][1]], [list[2][0][0], list[2][1]], [list[3][0][0], list[3][1]], [list[4][0][0], list[4][1]]] 
cpu1 = [[list[0][0][1], list[0][1]], [list[1][0][1], list[1][1]], [list[2][0][1], list[2][1]], [list[3][0][1], list[3][1]], [list[4][0][1], list[4][1]]]
cpu2 = [[list[0][0][2], list[0][1]], [list[1][0][2], list[1][1]], [list[2][0][2], list[2][1]], [list[3][0][2], list[3][1]], [list[4][0][2], list[4][1]]]


#list0 = [list[0][0][0], list[1][0][0], list[2][0][0], list[3][0][0], list[4][0][0]]
#list1 = [list[0][0][1], list[1][0][1], list[2][0][1], list[3][0][1], list[4][0][1]]
#list2 = [list[0][0][2], list[1][0][2], list[2][0][2], list[3][0][2], list[4][0][2]]


#x0 = float(sum(list0) /(len(list0)))
#y0 = max(list0)
#z0 = min(list0)
#RecordCount0 = len(list0)


#all = {'AverageValue: ':x0,'MaxValue: ':y0,'MinValue: ':z0,'RecordCount' :RecordCount0}


#print list
print cpu0
print cpu1
print cpu2
#print list0
#print list1
#print list2
#print all
