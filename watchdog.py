#!/usr/bin/env python

import sys, time, os
from daemon import Daemon
from subprocess import check_output
from os import system
from time import sleep

class MyDaemon(Daemon):
	def run(self):
		watchdog()

def watchdog():
	cmd = "ls /dev/ | grep ttyUSB"
	usb = check_output(cmd, shell=True)

	system("/root/./usbConfig.pl")

	while(1):
		if (usb != check_output(cmd, shell=True)):
			system("/root/./usbConfig.pl")
			usb = check_output(cmd, shell=True)
			system("service kplex restart")
		sleep(5)

if __name__ == "__main__":
	daemon = MyDaemon('/var/run/watchdogKplex.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)