#!/usr/bin/env python
import sys, os.path, urllib2
firstrun = 1
help = "Simply enter the name of the account and I will check if it already exists, if it doesnt ill back it up.\nCurrent options:\n[1:]\tEnter a name to make or restore a backup.\n[2:]\tHelp."
cocpath = '/data/data/com.supercell.clashofclans/shared_prefs/'
backuppath = '/sdcard/cswitcher/'
x = sys.argv[1]
def updater():
	currentversion = 0.3
	newversion = urllib2.urlopen("https://raw.githubusercontent.com/DevPhreak/cSwitch/master/Update.txt").read()
	if newversion > currentversion:
		answer = str(raw_input("There is a new version available, would you like to update?\nYes \\ No: "))
		if (answer == 'Yes' or answer =='Y' or answer == 'y' or answer == 'yes'):
		 os.system("curl -k -L -O http://raw.githubusercontent.com/DevPhreak/cSwitch/master/cswitch.py")
		else:
			print 'Ignoring update.'
			firstrun()
	else:
		print 'You\'re up-to-date'
		firstrun()
def killapp( appname ):
	print 'Killing app: %s'%appname
	os.system("su -c 'am kill %s'"%appname)
	return
def firstrun():
	if os.path.exists('/sdcard/cswitcher')	== True:
		firstrun = 0
		main()
	else:
		os.mkdir('/sdcard/cswitcher')
		print help
	return
def main():
	if x == 'help':,
		print help
	elif os.path.isfile(backuppath+x) == True:
		killapp( 'com.supercell.clashofclans' )
		print 'Restoring', x
		os.system("su -c 'cp -f %s%s %s/storage.xml'"%(backuppath, x, cocpath))
	else:
		print 'Going to backup current profile'
		os.system("su -c 'cp -f %s/storage.xml %s%s'"%(cocpath, backuppath, x))
updater()