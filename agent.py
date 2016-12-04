#!/usr/bin/python
import pyinotify,subprocess
from crontab import CronTab

ABS_PATH_AGENT_CONF_FILE='/root/spy_script_py/agentconfig.json'
def onChange(ev):
    cmd = ['/bin/echo',ABS_PATH_AGENT_CONF_FILE, ev.pathname, 'changed']
    subprocess.Popen(cmd).communicate()


if __name__ == '__main__':
	wm = pyinotify.WatchManager()
	wm.add_watch(ABS_PATH_AGENT_CONF_FILE, pyinotify.IN_MODIFY, onChange)
	notifier = pyinotify.Notifier(wm)
	notifier.loop()
