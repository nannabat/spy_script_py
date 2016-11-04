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
        ts_b = ts_a.write_bytes
        ts_c = ts_a.write_count
        ts_d = (ts_b/ts_c)
        ts_time_stamp = time.time()
        ts_st = datetime.datetime.fromtimestamp(ts_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
        ts_return_list.append(ts_st)
        ts_return_list.append(ts_d)
        return ts_return_list
def get_readbytes(): 
        a = psutil.disk_io_counters()
        b = a.write_bytes
        c = a.write_count
        d = (b/c)
        return d
disk_stats = []
disk_stats_with_timestamp = []
for i in range(1,6):
   time.sleep(5)
   disk_stats.append(get_readbytes())
   disk_stats_with_timestamp.append(get_readbytes_with_timestamp())







x = (sum(disk_stats) / float(len(disk_stats)))
y = max(disk_stats)
z = min(disk_stats)
RecordCount = len(disk_stats)
aa = "Logical Volume Manager" 
bb = "Total"
cc = "avg_disk_writebytes_write"
dd = "Avg.Disk Bytes/write"
ee = "20sec"


all = {'Duration: ':ee,'PerformanceCounterCategory: ':aa,'PerformanceCounterInstanceName: ':bb,'PerformanceCounterLabel: ':cc,'PerformanceCounterName: ':dd,'AverageValue: ':x,'MaxValue: ':y,'MinValue: ':z,'RecordCount: ':RecordCount,'HostName: ':var1,'ReportDateTime: ':var100,'IPAddress: ':ip_Address}

for k,v in sorted(all.items()):
	print k, v

value = {'Values':disk_stats_with_timestamp}
	
print json.dumps(value, indent=4)

