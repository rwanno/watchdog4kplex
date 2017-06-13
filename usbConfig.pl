#!/usr/bin/perl
#This program write the file /etc/kplex.conf when the NMEA devices are remove or add

use strict;
use warnings;

my @USB = `ls /dev/ | grep ttyUSB`;
my $cheminConf = "/etc/kplex.conf";

open (my $fhConf, ">", "$cheminConf")
	|| die "Erreur: $!\n";

foreach my $usb (@USB) {
	chomp $usb;
	print $fhConf "\n#configuration $usb\n[serial]\nfilename=/dev/$usb\ndirection=in\nbaud=4800\n";
}

#
print $fhConf "
[tcp]
mode=server
port=10110
direction=out
";

close $fhConf;

exit 0;