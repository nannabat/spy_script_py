import subprocess
import datetime
import json
import socket
import fcntl
import struct
import psutil
import time
import datetime



def get_mount_and_device():
    mount_and_device = {}
    for disk_obj in psutil.disk_partitions():
        mount_and_device[disk_obj.mountpoint] = disk_obj.device
    return mount_and_device

#print get_mount_and_device()

a = ['/', '/boot']


def get_readbytes():
    ts_return_list = []
    ts_a = psutil.disk_usage(a[0])
    ts_b = ts_a.used
    ts_time_stamp = time.time()
    ts_st = datetime.datetime.fromtimestamp(ts_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    ts_c = psutil.disk_usage(a[1])
    ts_d = ts_c.used
    ts_time_stamp1 = time.time()
    ts_st1 = datetime.datetime.fromtimestamp(ts_time_stamp1).strftime('%Y-%m-%d %H:%M:%S')
    ts_return_list.append(ts_b)
    ts_return_list.append(ts_st)
    ts_return_list.append(ts_d)
    ts_return_list.append(ts_st1)
   
    return ts_return_list
    
print get_readbytes()

     
