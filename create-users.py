#!/usr/bin/python2
import os
import re
import sys

def main():
	for line in sys.stdin:
		match = re.match("#",line)
		fields = line.strip().split(':')
		
		if match or len(fields) != 5:
			continue
		username = fields[0]
		password = fields[1]

		gecos = "%s %s,,," % (fields[3],fields[2])

		groups = fields[4].split(',')

		print ("==> Creating account for %s...." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
		#print("command ran was: ", cmd)
		os.system(cmd)
		print("==> Setting the password for %s..." % (username))
		#print cmd
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
		#print("command ran was ", cmd)
		os.system(cmd)
		for group in groups:
			if group != '-':
				print "==> Assingning %s to the %s group...." % (username,group)
				cmd = "/usr/sbin/adduser %s %s" % (username,group)
				#print("command ran was ", cmd)
				os.system(cmd)
				#print cmd
				os.system(cmd)
		
if __name__ == '__main__':
	main()
