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

import os, sys

from FireModules.fire_module_base_class import *

class os_osx_applescript_command( FireModule ):

	def __init__(self):
		self.commentsStr = "OSCommand/os_osx_applescript_command"
		self.commandStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "OSCommand/os_osx_applescript_command"
		self.commandStr = ""
		return;

	def Description( self ):
		self.Description = "Runs the AppleScript command (via 'oasscript()') supplied in configuration setting"
		return self.Description

        def Configure( self ):
		print "Example Applscript command: tell app \"Finder\" to display dialog \"Never Gonna Give You Up!\""
                self.commandStr = raw_input( "Applescript Command: " )
                return

        def GetParameters( self ):
                return( self.commandStr )

        def SetParameters( self, parametersStr ):
                self.commandStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

                if ( self.commandStr == "" ):
                        print "## ", self.commentsStr, ": Error - OS command string is blank"
                        return

		else:
			print self.commentsStr + ": Running OS command => " + self.commandStr
			self.osaCommandStr = "osascript -e '" + self.commandStr + "'"
			os.system( self.osaCommandStr )

		return

