#!/usr/bin/python
import pyinotify,subprocess
from crontab import CronTab
def onChange(ev):
    cmd = ['/bin/echo', '/root/spy_script_py/agentconfig.json', ev.pathname, 'changed']
    subprocess.Popen(cmd).communicate()
wm = pyinotify.WatchManager()
wm.add_watch('/root/spy_script_py/agentconfig.json', pyinotify.IN_MODIFY, onChange)
notifier = pyinotify.Notifier(wm)
notifier.loop()
