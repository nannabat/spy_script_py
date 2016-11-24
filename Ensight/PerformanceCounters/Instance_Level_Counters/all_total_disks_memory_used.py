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

log_file_name_text = '_avg_total_disk_used_'

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




def get_mount_and_device():
    mount_and_device = {}
    for disk_obj in psutil.disk_partitions():
        mount_and_device[disk_obj.mountpoint] = disk_obj.device
    return mount_and_device



def get_readbytes_with_timestamp():
        ts_return_list = []
        ts_a = psutil.disk_usage('/')
        ts_b = ts_a.used
        ts_d = (ts_b/(1024*1024))
        ts_time_stamp = time.time()
        ts_st = datetime.datetime.fromtimestamp(ts_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
        ts_return_list.append(ts_st)
        ts_return_list.append(ts_d)
        return ts_return_list
def get_readbytes():
        #return_list = []
        a = psutil.disk_usage('/')
        b = a.used
        d = (b/(1024*1024)) 
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
aa = "Mounted Disks"
bb = "mount point"
cc = "avg_total_megabytes_used"
dd = "Avg_Total_MegaBytes_Used"
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
  
value = {'Values':disk_stats_with_timestamp}
  
print json.dumps(value, indent=4)
values_variable = json.dumps(value,indent=4)
print >> file_handler,values_variable

file_handler.close()





	

