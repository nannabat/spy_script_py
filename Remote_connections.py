import psutil
import subprocess
def ip_to_hostname(ip_addr):
  cmd_hostname = 'nslookup ' + ip_addr
  nslkup_output = subprocess.check_output(cmd_hostname,shell=True)


def get_active_connections():
  active_connections= []
  for connection in psutil.net_connections():
    tmp_active_connection = {}
    if connection.type == 1:
      tmp_active_connection['Connection_Type'] = 'TCP'
      tmp_active_connection['Local_Port'] = connection.laddr[1]
      tmp_active_connection['LocalIP'] = connection.laddr[0]
      #tmp_active_connection['ReportDateTime'] = var100
      #tmp_active_connection['LocalHostName'] = va1
      if not connection.raddr:
        tmp_active_connection['RemoteIP'] = 'Null'
        tmp_active_connection['Remote-Port'] = 'Null'
      else:
        tmp_active_connection['RemoteIP'] = connection.raddr[0]
        tmp_active_connection['Remote_Port'] = connection.raddr[1]

    elif connection.type  == 2:
      tmp_active_connection['Connection_Type'] = 'UDP'
      tmp_active_connection['Local_Port'] = connection.laddr[1]
      tmp_active_connection['LocalIP'] = connection.laddr[0]
      #tmp_active_connection['ReportDateTime'] = var100
      #tmp_active_connection['LocalHostName'] = va1
      if not connection.raddr:
        tmp_active_connection['RemoteIP'] = 'Null'
        tmp_active_connection['Remote-Port'] = 'Null'
      else:
        tmp_active_connection['RemoteIP'] = connection.raddr[0]
        tmp_active_connection['Remote-Port'] = connection.raddr[1]
        
    else:
      tmp_active_connection['Connection_Type'] = connection.type
      tmp_active_connection['Local_Port'] = connection.laddr[1]
      tmp_active_connection['LocalIP'] = connection.laddr[0]
      if not connection.raddr:
        tmp_active_connection['RemoteIP'] = 'Null'
        tmp_active_connection['Remote-Port'] = 'Null'
      else:
        tmp_active_connection['RemoteIP'] = connection.raddr[0]
        tmp_active_connection['Remote-Port'] = connection.raddr[1]
        
    active_connections.append(tmp_active_connection)
  #print active_connections
  return active_connections

# connections = get_active_connections()
# all = {'active_connections':connections}
# #print all

#print json.dumps(all, indent=4)
