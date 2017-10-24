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

import sys, subprocess

from FireModules.fire_module_base_class import *

class os_win_powershell_script( FireModule ):

	def __init__(self):
		self.commentsStr = "OSCommand/os_win_powershell_script"
		self.psScriptFilepathStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "OSCommand/os_win_powershell_script"
		self.psScriptFilepathStr = ""
		return;

	def Description( self ):
		self.Description = "Runs the Windows Powershell script file supplied in configuration setting"
		return self.Description

        def Configure( self ):
                self.tempStr = raw_input( "Powershell script filepath (ex. C:\Users\USER\Scripts\myscript.ps1 ): " )

		# Add extra '\' to each occurrence of backslash in filepath
		# Python wants to see "C:\\Users\\USER\\Scripts\\myscript.ps1"
		# But I'd never expect a user to have to type that in. Because lame.
		self.psScriptFilepathStr = self.tempStr.replace( '\\', '\\\\' )

		# Let them know what happened
		print ""
		print "** Added backslash escapes to filepath for you, otherwise Python gets sad when loading file"
		print "** Stored filepath =", self.psScriptFilepathStr

                return

        def GetParameters( self ):
                return( self.psScriptFilepathStr )

        def SetParameters( self, parametersStr ):
                self.psScriptFilepathStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

                if ( self.psScriptFilepathStr == "" ):
                        print "## ", self.commentsStr, ": Error - Powershell script filepath is blank"
                        return

		else:
			print self.commentsStr + ": Executing Powershell script  => " + self.psScriptFilepathStr

			self.process = subprocess.Popen([ "powershell.exe", self.psScriptFilepathStr ], stdout=sys.stdout )

			# Make sure we see the output on stdout, and wait for process to finish executing
			self.process.communicate()

		return

