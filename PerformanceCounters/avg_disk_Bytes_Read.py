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



def get_dna():
    name = subprocess.check_output("hostname | cut -d'.' -f1", shell=True)
    return name
var1 = get_dna()

def get_tm():
       a = datetime.datetime.now()
       return str(a)
var100 = get_tm()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip_Address = get_ip_address('eth0')


def get_readbytes_with_timestamp():
        ts_return_list = []
        ts_a = psutil.disk_io_counters()
        ts_b = ts_a.read_bytes
        ts_c = ts_a.read_count
        ts_d = (ts_b/ts_c)
        ts_time_stamp = time.time()
        ts_st = datetime.datetime.fromtimestamp(ts_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
#        ts_return_list['DateTime'] = ts_d
#        ts_return_list['Value'] = ts_st
        ts_return_list.append(ts_st)
        ts_return_list.append(ts_d)
        return ts_return_list
def get_readbytes():
        #return_list = []
        a = psutil.disk_io_counters()
        b = a.read_bytes
        c = a.read_count
        d = (b/c)
        #return_list.append(d)
        return d
#var10 = get_readbytes()
disk_stats = []
disk_stats_with_timestamp = []
for i in range(1,6):
   time.sleep(5)
   #r_bytes_value = get_readbytes()
   #r_bytes_with_timestamp = get_readbytes_with_timestamp()
   disk_stats.append(get_readbytes())
   disk_stats_with_timestamp.append(get_readbytes_with_timestamp())

#print disk_stats
#print disk_stats_with_timestamp




x = (sum(disk_stats) / float(len(disk_stats)))
y = max(disk_stats)
z = min(disk_stats)
RecordCount = len(disk_stats)
aa = "Logical Volume Manager" 
bb = "Total"
cc = "avg_disk_readbytes_Read"
dd = "Avg.Disk Bytes/Read"
ee = "20sec"
all = {'Duration: ':ee,'PerformanceCounterCategory: ':aa,'PerformanceCounterInstanceName: ':bb,'PerformanceCounterLabel: ':cc,'PerformanceCounterName: ':dd,'AverageValue: ':x,'MaxValue: ':y,'MinValue: ':z,'RecordCount: ':RecordCount,'HostName: ':var1,'ReportDateTime: ':var100,'IPAddress: ':ip_Add}
od_all = collections.OrderedDict(sorted(all.items()))
print json.dumps(od_all, indent=4)


# for k,v in sorted(all.items()):
# 	print k, v

value = {'Values':disk_stats_with_timestamp}
	
print json.dumps(value, indent=4)

