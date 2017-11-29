#!/usr/bin/python
#
# Filename:  osx_chicken_loop_youtube_video.py
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
#	Opens a 10-hour chicken sounds loop on Youtube in the default browser
#

import os, sys

from FireModules.fire_module_base_class import *

class osx_chicken_loop_youtube_video( FireModule ):

	def __init__(self):
		self.commentsStr = "Shenanigans/osx_chicken_loop_youtube_video"
		self.textToSayStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/osx_chicken_loop_youtube_video"
		self.textToSayStr = ""
		return;

	def Description( self ):
		self.Description = "Opens default browser and starts YouTube 10-hour loop of chicken sounds. After turning system volume up to maximum."
		return self.Description

        def Configure( self ):
                self.configStr = "(None)"
                return

        def GetParameters( self ):
                return( self.configStr )

        def SetParameters( self, parametersStr ):
                # Nothing to set, does not take parameters, so just return
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

		print self.commentsStr + ": Setting system audio to max volume"
		os.system( "osascript -e 'set volume output volume 100'")

		print self.commentsStr + ": Opening 10-hour loop of chicken sounds on Youtube"
		self.commandStr = "open https://www.youtube.com/watch?v=E9BQAAT10Mwi"
		os.system( self.commandStr )

		return

