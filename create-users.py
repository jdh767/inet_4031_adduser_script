#!/usr/bin/python2
import os
import re
import sys

def main():
	for line in sys.stdin:
		match = re.match("#",line)
		fields = line.strip().split(':')
		
		if match or len(fields) != 5: # We are checking if the line is valid to be processed because 
						# if it is a comment and starts with a # or does not have 5
						# valid fields then it cannot be processed and should be skipped.
						# This is important because we would not want to create a user 
						# that is not meant to be utilized.
			continue
		username = fields[0]
		password = fields[1]

		gecos = "%s %s,,," % (fields[3],fields[2])

		groups = fields[4].split(',') # this line splits the field[4] the groups field by the comma if present
						# This is meant so that if a user needs to be added to multiple groups 
						# We can split the groups by a comma in order to put them in the right place

		print ("==> Creating account for %s...." % (username))
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
		#print("command ran was: ", cmd)
		os.system(cmd) # The purpose of this line is to execute the string into the command line which this case would be
				# to add a user using the cmd
		print("==> Setting the password for %s..." % (username))
		#print cmd
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
		#print("command ran was ", cmd)
		os.system(cmd)
		for group in groups: # In this line we are looping if the user is meant to be assigned to multiple groups when split earlier
			if group != '-':
				print "==> Assingning %s to the %s group...." % (username,group)
				cmd = "/usr/sbin/adduser %s %s" % (username,group)
				#print("command ran was ", cmd)
				os.system(cmd)
				#print cmd
				os.system(cmd)
		
if __name__ == '__main__':
	main()
