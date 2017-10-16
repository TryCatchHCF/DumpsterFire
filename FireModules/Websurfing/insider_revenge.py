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

import urllib2

from FireModules.fire_module_base_class import *

class insider_revenge( FireModule ):

	def __init__(self):
		self.commentsStr = "insider_revenge"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "insider_revenge"
		return;

	def Description( self ):
		self.Description = "Opens various Websites that may be associated with insider threat"
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

		print self.commentsStr + ": Opening URL session to <...>"

		#webSession = urllib2.urlopen( 'https://www.facebook.com' )
		#trash = webSession.read()

		return

