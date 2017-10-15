#!/usr/bin/python
#
# Filename:  osx_rickroll_open_youtube_video.py
#
# Version: 1.0.0
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:
#
#
# Description:
#
#	Opens the Wikipedia page for Rick Astley, using the system default browser,
#	brings it into foreground.
#

import os, sys

from FireModules.fire_module_base_class import *

class osx_rickroll_open_youtube_video( FireModule ):

	def __init__(self):
		self.commentsStr = "Shenanigans/osx_rickroll_open_youtube_video"
		self.textToSayStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/osx_rickroll_open_youtube_video"
		self.textToSayStr = ""
		return;

	def Description( self ):
		self.Description = "Opens Wikipedia Rick Astley webpage"
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

		print self.commentsStr + ": Opening Rick Astley Youtube video"
		self.commandStr = "open https://www.youtube.com/watch?v=dQw4w9WgXcQ"
		os.system( self.commandStr )

		return

