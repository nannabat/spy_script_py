#!/usr/bin/python
import pyinotify,subprocess
from crontab import CronTab

ABS_PATH_AGENT_CONF_FILE='/root/spy_script_py/agentconfig.json'
CONF_MODIFIED=False



def onChange(ev):
    cmd = ['/bin/echo',ABS_PATH_AGENT_CONF_FILE, ev.pathname, 'changed']
    subprocess.Popen(cmd).communicate()
    CONF_MODIFIED = True
    if CONF_MODIFIED == True:
    	config_file = open('agentconfig.json','r')
    	configurations = json.load(config_file)
    	for scriptname,time_value in configurations.items():
    		print 'for ' + scriptname + ' the time value set is: ' +  time_value

def get_intial_values_list():
	config_file = open(ABS_PATH_AGENT_CONF_FILE,'r')
	configurations = json.load(config_file)
	return_dict_intial_values = {}
	for scriptname,time_value in configurations.items():
		return_dict_intial_values[scriptname] = time_value
	return return_dict_intial_values
		



    		
if __name__ == '__main__':
	wm = pyinotify.WatchManager()
	wm.add_watch(ABS_PATH_AGENT_CONF_FILE, pyinotify.IN_MODIFY, onChange)
	notifier = pyinotify.Notifier(wm)
	print "the value of CONF_MODIFIED: " + str(CONF_MODIFIED)
	print get_intial_values_list
	notifier.loop()

		
