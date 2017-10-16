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

import urllib, time, random

from FireModules.fire_module_base_class import *

class warez_sites( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/warez_sites"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/warez_sites"
		return;

	def Description( self ):
		self.Description = "Visits TorProject.org site and various pages"
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

		print self.commentsStr + ": Opening URL session to DirtyWarez.org landing page"
		self.webSession = urllib.urlopen( 'http://www.dirtywarez.org' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to WarezCrack.net page"
		self.webSession = urllib.urlopen( 'https://warezcrack.net/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to PCWarez.org landing page"
		self.webSession = urllib.urlopen( 'https://pcwarez.org' )
		trash = self.webSession.read()

		return


	def SleepSession( self ):

		# Random sleep from 5-100 seconds, because humans read
		seconds = random.randint( 5, 100 )
		print "Sleeping for", seconds, "seconds to simulate human browsing habits"
		time.sleep( seconds )

		return
