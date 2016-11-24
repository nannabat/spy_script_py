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



log_file_name_text = '_avg_bytes_recived_nics_'


def get_dna():
    name = subprocess.check_output("hostname | cut -d'.' -f1", shell=True)
    return name
var1 = get_dna()

def get_tm():
       a = datetime.datetime.now()
       return str(a)
var100 = get_tm()

def get_ip_address():
        
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       s.connect(('google.com', 0))
       ip = s.getsockname()[0]
       return ip
ip_Address = get_ip_address() 

def get_readbytes_with_timestamp():
        ts_return_list = []
        ts_a = psutil.net_io_counters()
        ts_d = ts_a.bytes_recv
        ts_time_stamp = time.time()
        ts_st = datetime.datetime.fromtimestamp(ts_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
        ts_return_list.append(ts_st)
        ts_return_list.append(float(ts_d))
        return ts_return_list


disk_stats_with_timestamp = []

for i in range(1,6):
   time.sleep(5)
   disk_stats_with_timestamp.append(get_readbytes_with_timestamp())

disk_stats = [disk_stats_with_timestamp[0][1], disk_stats_with_timestamp[1][1],disk_stats_with_timestamp[2][1], disk_stats_with_timestamp[3][1],disk_stats_with_timestamp[4][1]]


x = float(sum(disk_stats) /(len(disk_stats)))
y = max(disk_stats)
z = min(disk_stats)
RecordCount = len(disk_stats)
aa = "Nics" 
bb = "Total"
cc = "avg_bytes_recived_nics"
dd = "Avg.Bytes_Recived_Nics"
ee = "20sec"


all = {'Duration: ':ee,'PerformanceCounterCategory: ':aa,'PerformanceCounterInstanceName: ':bb,'PerformanceCounterLabel: ':cc,'PerformanceCounterName: ':dd,'AverageValue: ':x,'MaxValue: ':y,'MinValue: ':z,'RecordCount: ':RecordCount,'HostName: ':var1,'ReportDateTime: ':var100,'IPAddress: ':ip_Address}


od_all = collections.OrderedDict(sorted(all.items()))
#timestamp = str(datetime.datetime.now()).replace(' ','_')
timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = os.path.expanduser("~") + '/' + var1.strip() + log_file_name_text + timestamp + '.json'
print filename
file_handler = open(filename,'a+') 
text_json = json.dumps(od_all, indent=4)
print >> file_handler,text_json


print json.dumps(od_all, indent=4)


# for k,v in sorted(all.items()):
#   print k, v

value = {'Values':disk_stats_with_timestamp}
  
print json.dumps(value, indent=4)
values_variable = json.dumps(value,indent=4)
print >> file_handler,values_variable

file_handler.close()


	

