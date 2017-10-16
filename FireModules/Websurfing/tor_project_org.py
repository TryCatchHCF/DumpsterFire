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

class tor_project_org( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/tor_project_org"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/tor_project_org"
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

		print self.commentsStr + ": Opening URL session to Tor Project landing page"
		self.webSession = urllib.urlopen( 'https://www.torproject.org/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to Tor Project blog page"
		self.webSession = urllib.urlopen( 'https://blog.torproject.org/' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to Tor Browser page"
		self.webSession = urllib.urlopen( 'https://www.torproject.org/projects/torbrowser.html' )
		trash = self.webSession.read()

		return


	def SleepSession( self ):

		# Random sleep from 5-100 seconds, because humans read
		seconds = random.randint( 5, 100 )
		print "Sleeping for", seconds, "seconds to simulate human browsing habits"
		time.sleep( seconds )

		return
