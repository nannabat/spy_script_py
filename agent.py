#!/usr/bin/python
import pyinotify,subprocess,json
from crontab import CronTab

ABS_PATH_AGENT_CONF_FILE='/root/spy_script_py/agentconfig.json'
CONF_MODIFIED=False
intial_value_list = {}



def onChange(ev):
    cmd = ['/bin/echo',ABS_PATH_AGENT_CONF_FILE, ev.pathname, 'changed']
    subprocess.Popen(cmd).communicate()
    CONF_MODIFIED = True
    print 'changed values are:'
    for script_name,time_value in get_changed_values_dict().items:
    	print scriptname + ':' + time_value

def get_values_list():
	config_file = open(ABS_PATH_AGENT_CONF_FILE,'r')
	configurations = json.load(config_file)
	return_dict_intial_values = {}
	for scriptname,time_value in configurations.items():
		return_dict_values[scriptname] = time_value
	return return_dict_values

def get_changed_values_dict():
	current_values_dict = get_values_list()
	return_changed_values_dict = {}
	for script_name in current_values_dict.keys():
		if intial_value_list[scriptname] == current_values_dict[scriptname]:
			return_changed_values_dict[scriptname] = current_values_dict[scriptname]
	intial_value_list = current_values_dict
	return return_changed_values_dict





		



    		
if __name__ == '__main__':
	wm = pyinotify.WatchManager()
	wm.add_watch(ABS_PATH_AGENT_CONF_FILE, pyinotify.IN_MODIFY, onChange)
	notifier = pyinotify.Notifier(wm)
	#print "the value of CONF_MODIFIED: " + str(CONF_MODIFIED)
	intial_value_list = get_values_list()
	notifier.loop()

		
