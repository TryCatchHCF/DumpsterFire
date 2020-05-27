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

class osx_say_text( FireModule ):

	def __init__(self):
		self.commentsStr = "Shenanigans/osx_say_text"
		self.textToSayStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/osx_say_text"
		self.textToSayStr = ""
		return;

	def Description( self ):
		self.Description = "Runs OSX terminal's 'say' command, speaks the configured string"
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
                print(self.commentsStr + ": Setting Logging flag!")
                print(logFlag)
                return

        def Ignite( self ):

                if ( self.textToSayStr == "" ):
                        print("## ", self.commentsStr, ": Error - Speech string is blank")
                        return

		else:
			print(self.commentsStr + ": Setting system audio to max volume")
			os.system( "osascript -e 'set volume output volume 100'")

			print(self.commentsStr + ": Speaking the following text => " + self.textToSayStr)
			self.sayStr = "say " + self.textToSayStr 
			os.system( self.sayStr )

		return

