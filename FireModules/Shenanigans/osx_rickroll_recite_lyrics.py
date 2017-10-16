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

class osx_rickroll_recite_lyrics( FireModule ):

	def __init__(self):
		self.commentsStr = "Shenanigans/osx_rickroll_recite_lyrics"
		self.textToSayStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/osx_rickroll_recite_lyrics"
		self.textToSayStr = ""
		return;

	def Description( self ):
		self.Description = "Runs OSX terminal's 'say' command, speaks lyrics from Rick Astley's Never Gonna Give You Up"
		return self.Description

        def Configure( self ):
                self.textToSayStr = raw_input( "Text to speak: " )
                return

        def GetParameters( self ):
                return( self.textToSayStr )

        def SetParameters( self, parametersStr ):
                self.textToSayStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

                if ( self.textToSayStr == "" ):
                        print "## ", self.commentsStr, ": Error - Speech string is blank"
                        return

		else:
			print self.commentsStr + ": Speaking the lyrics from Rick Astley's Never Gonna Give You Up"
			self.textToSayStr = ""
			self.sayStr = "say " + self.textToSayStr 
			os.system( self.sayStr )

		return

