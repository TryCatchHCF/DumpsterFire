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

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/osx_rickroll_recite_lyrics"
		return;

	def Description( self ):
		self.Description = "Runs OSX terminal's 'say' command, speaks lyrics from Rick Astley's Never Gonna Give You Up. After tunrning system volume up to maximum."
		return self.Description

        def Configure( self ):
                return

        def GetParameters( self ):
                return( "" )

        def SetParameters( self, parametersStr ):
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

		print self.commentsStr + ": Setting system audio to max volume"
		os.system( "osascript -e 'set volume output volume 100'")

		print self.commentsStr + ": Speaking the lyrics from Rick Astley's Never Gonna Give You Up"

		self.sayStr = "say " + "Never gonna give you up"
		os.system( self.sayStr )

		self.sayStr = "say " + "Never gonna let you down"
		os.system( self.sayStr )

		self.sayStr = "say " + "Never gonna run around and desert you"
		os.system( self.sayStr )

		self.sayStr = "say " + "Never gonna make you cry"
		os.system( self.sayStr )

		self.sayStr = "say " + "Never gonna say goodbye"
		os.system( self.sayStr )

		self.sayStr = "say " + "Never gonna tell a lie"
		os.system( self.sayStr )

		self.sayStr = "say " + "And hurt you"
		os.system( self.sayStr )

		return


