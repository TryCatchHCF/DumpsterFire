#!/usr/bin/python
#
# Filename:  
#
# Version: 1.0.0
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:
#
#	Part of the DumpsterFire Toolset. See documentation at https://github.com/TryCatchHCF/DumpsterFire
#
#
# Description:
#
#
# Example:
#
#

import urllib, time, random

from FireModules.fire_module_base_class import *

class hacking_sites( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/hacking_sites"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/hacking_sites"
		return;

	def Description( self ):
		self.Description = "Opens a few hacking websites to generate Web traffic"
		return self.Description

	def Configure( self ):
		return

	def GetParameters( self ):
		return ""

	def SetParameters( self, parametersStr ):
		print parametersStr
		return

	def ActivateLogging( self, logFlag ):
		print self.commentsStr + ": Setting Logging flag!"
		print logFlag
		return

	def Ignite( self ):

		print self.commentsStr + ": Opening URL session to ExploitDB landing page"
		self.webSession = urllib.urlopen( 'https://www.exploit-db.com/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to ExploitDB exploits"
		self.webSession = urllib.urlopen( 'https://www.exploit-db.com/browse/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to ExploitDB Google hacking DB"
		self.webSession = urllib.urlopen( 'https://www.exploit-db.com/google-hacking-database/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to SecList FullDisclosure site"
		self.webSession = urllib.urlopen( 'http://seclists.org/fulldisclosure/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to Shodan (systems with default passwords)"
		self.webSession = urllib.urlopen( 'https://www.shodan.io/search?query=%22default+password%22' )
		trash = self.webSession.read()

		return


	def SleepSession( self ):

		# Random sleep from 5-100 seconds, because humans read
		seconds = random.randint( 5, 100 )
		print "Sleeping for", seconds, "seconds to simulate human browsing habits"
		time.sleep( seconds )

		return
