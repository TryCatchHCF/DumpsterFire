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

class online_gambling( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/online_gambling"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/online_gambling"
		return;

	def Description( self ):
		self.Description = "Visits various online gambling sites"
		return self.Description

	def Configure( self ):
		return

	def GetParameters( self ):
		return ""

	def SetParameters( self, parametersStr ):
		print self.commentsStr + ": Setting parameters!"
		print parametersStr
		return

	def ActivateLogging( self, logFlag ):
		print self.commentsStr + ": Setting Logging flag!"
		print logFlag
		return

	def Ignite( self ):

		print self.commentsStr + ": Opening URL session to GamblingSites.org landing page"
		self.webSession = urllib.urlopen( 'https://www.gamblingsites.org' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to CaesarsCasino.com landing page"
		self.webSession = urllib.urlopen( 'https://www.caesarscasino.com' )
		trash = self.webSession.read()

		self.SleepSession()

		print self.commentsStr + ": Opening URL session to CasinoAus.com landing page"
		self.webSession = urllib.urlopen( 'https://www.casinoaus.com' )
		trash = self.webSession.read()

		return


	def SleepSession( self ):

		# Random sleep from 5-100 seconds, because humans read
		seconds = random.randint( 5, 100 )
		print "Sleeping for", seconds, "seconds to simulate human browsing habits"
		time.sleep( seconds )

		return
