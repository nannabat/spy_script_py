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



log_file_name_text = '_perc_processor_time_instance_00_'

def get_proc():
    number = subprocess.check_output("cat /proc/cpuinfo | grep processor | wc -l", shell=True)
    return number
cpunumber = get_proc()



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
     time.sleep(1)
     list.append(get_allcpu())


values = [list[0][0][0], list[0][1], list[1][0][0], list[1][1], list[2][0][0], list[2][1], list[3][0][0], list[3][1], list[4][0][0], list[4][1]]
#cpu1 = [[list[0][0][1], list[0][1]], [list[1][0][1], list[1][1], [list[2][0][1], list[2][1]], [list[3][0][1], list[3][1]], [list[4][0][1]], list[4][1]]]
#cpu2 = [[list[0][0][2], list[0][1]], [list[1][0][2], list[1][1], [list[2][0][2], list[2][1]], [list[3][0][2], list[3][1]], [list[4][0][2]], list[4][1]]]

list0 = [list[0][0][0], list[1][0][0], list[2][0][0], list[3][0][0], list[4][0][0]]



avg_value = float(sum(list0)/(len(list0)))
maximum = max(list0)
minimum = min(list0)
count = len(list0)

aa = "Cpu Percentage used"
bb = "Instance"
cc = "avg_cpu_percent"
dd = "avg.cpu_percent_used"
ee = "20sec"


all = {'Duration: ':ee,'PerformanceCounterCategory: ':aa,'PerformanceCounterInstanceName: ':bb,'PerformanceCounterLabel: ':cc,'PerformanceCounterName: ':dd,'AverageValue: ':avg_value,'MaxValue: ':maximum,'Minimum: ':minimum,'RecordCount: ':count,'HostName: ':var1,'ReportDateTime: ':var100,'IPAddress: ':ip_Address}



od_all = collections.OrderedDict(sorted(all.items()))
#timestamp = str(datetime.datetime.now()).replace(' ','_')
timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = os.path.expanduser("~") + '/' + var1.strip() + log_file_name_text + timestamp + '.json'

print filename
file_handler = open(filename,'a+') 
text_json = json.dumps(od_all, indent=4)
print >> file_handler,text_json

print json.dumps(od_all, indent=4)
  
value = {'Values':values}
  
print json.dumps(value, indent=4)
values_variable = json.dumps(value,indent=4)
print >> file_handler,values_variable

file_handler.close()






