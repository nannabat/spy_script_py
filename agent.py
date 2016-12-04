#!/usr/bin/python
import pyinotify,subprocess
from crontab import CronTab

ABS_PATH_AGENT_CONF_FILE='/root/spy_script_py/agentconfig.json'
CONF_MODIFIED=False



def onChange(ev):
    cmd = ['/bin/echo',ABS_PATH_AGENT_CONF_FILE, ev.pathname, 'changed']
    subprocess.Popen(cmd).communicate()
    CONF_MODIFIED = True


if __name__ == '__main__':
	wm = pyinotify.WatchManager()
	wm.add_watch(ABS_PATH_AGENT_CONF_FILE, pyinotify.IN_MODIFY, onChange)
	notifier = pyinotify.Notifier(wm)
	print "the value of CONF_MODIFIED: " + str(CONF_MODIFIED)
	notifier.loop()
	if CONF_MODIFIED == True:
		config_file = open('agentconfig.json','r')
		configurations = json.load(config_file)
		for scriptname,time_value in configurations.items():
			print 'for ' + scriptname + ' the time value set is: ' +  time_value
		
