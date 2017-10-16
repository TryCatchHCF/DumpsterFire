#!/usr/bin/python
#
# Filename:  
#
# Version: 1.0.0
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:  Attempts to connect to various pornography sites. Useful for testing network filters & alerts.
#
#	Part of the DumpsterFire Toolset. See documentation at https://github.com/TryCatchHCF/DumpsterFire
#
#
# Description:
#
#

import urllib, time, random

from FireModules.fire_module_base_class import *

class porn_sites( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/porn_sites"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/porn_sites"
		return;

	def Description( self ):
		self.Description = "Opens a few porn websites to generate Web traffic , test filters"
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

		print self.commentsStr + ": Opening URL session to PornHub landing page"
		self.webSession = urllib.urlopen( 'https://www.pornhub.com/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to RedTube landing page"
		self.webSession = urllib.urlopen( 'https://www.redtube.com/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to PornTube landing page"
		self.webSession = urllib.urlopen( 'https://www.porntube.com/' )
		trash = self.webSession.read()

		return


	def SleepSession( self ):

		# Random sleep from 5-100 seconds, because humans read
		seconds = random.randint( 5, 100 )
		print "Sleeping for", seconds, "seconds to simulate human browsing habits"
		time.sleep( seconds )

		return
