The aim of this program is to add a dynamical configuration for the NMEA multiplexer Kplex. 
It was tested only under Raspbian, on Raspberry pi 3. This daemon use systemd (to run watchdog before Kplex), and it's doesn't work systemV systems.

I use github for the first time (for school project) and I using python recently, sorry for the lot of mistakes that you will find.

You need to have kplex for use this program.
If your kplex work under systemV (/etc/init.d), you need to disable this init file :

update-rc.d kplex disable
update-rc.d kplex remove

Now you can proceed to the install:
1) Get the repository and extract them
2) Put watchdog.py and daemon.py into /usr/bin/ directory
3) Put watchdog4kplex.service and kplex.service in /lib/systemd/system/
4) run this commands lines to enable services:
	- systemctl enable watchdog4kplex.service
	- systemctl enable kplex.service
	- systemctl daemon-reload

