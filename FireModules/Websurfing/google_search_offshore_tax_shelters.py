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

class google_search_offshore_tax_shelters( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/google_search_offshore_tax_shelters"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/google_search_offshore_tax_shelters"
		return;

	def Description( self ):
		self.Description = "Performs Google search on offshore tax shelters"
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

		print self.commentsStr + ": Opening URL session for Google search on offshore tax shelters"
		self.webSession = urllib.urlopen( 'https://www.google.com/search?q=offshore+tax+shelters&oq=offshore+tax+shelters' )
		trash = self.webSession.read()

		return

