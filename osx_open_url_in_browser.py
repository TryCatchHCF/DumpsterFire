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

import os, sys, urllib

from FireModules.fire_module_base_class import *

class osx_open_url_in_browser( FireModule ):

	def __init__(self):
		self.commentsStr = "Shenanigans/osx_open_url_in_browser"
		self.mURL = "https://www.google.com/search?&q=meerkats&oq=meerkats"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/osx_open_url_in_browser"
		self.mURL = "https://www.google.com/search?&q=meerkats&oq=meerkats"
		return;

	def Description( self ):
		self.Description = "Opens the configured URL in the system's default Web browser. Defaults to a Google search for meerkats. Because meerkats are amazing."
		return self.Description

	def Configure( self ):
		self.mURL = raw_input( "Enter URL to open in Web browser: " )
		return

	def GetParameters( self ):
		return self.mURL

	def SetParameters( self, parametersStr ):
		self.mURL = parametersStr
		return

	def ActivateLogging( self, logFlag ):
		print self.commentsStr + ": Setting Logging flag!"
		print logFlag
		return

	def Ignite( self ):

		print self.commentsStr + ": Opening default system Web browser with URL: " + self.mURL

		self.commandStr = "open " + self.mURL
		os.system( self.commandStr )


		return

