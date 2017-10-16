#!/usr/bin/python
#
# Filename:  osx_rickroll_multi_dialogs.py
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
#	Opens a series of dialogs, each with one rickroll line, preceded by 
#	whatever the current alert sound is set to. No default button set,
#	forcing them to click through.
#

import os, sys

from FireModules.fire_module_base_class import *

class osx_rickroll_multi_dialogs( FireModule ):

	def __init__(self):
		self.commentsStr = "Shenanigans/osx_rickroll_multi_dialogs"
		self.textToSayStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/osx_rickroll_multi_dialogs"
		self.textToSayStr = ""
		return;

	def Description( self ):
		self.Description = "Opens a series of dialogs, each with one rickroll line."
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

		print self.commentsStr + ": Spawning rickrolling dialogs"
		self.beepStr = "osascript -e beep"

		os.system( self.beepStr )
		self.commandStr = "osascript -e 'tell app \"System Events\" to display dialog \"Never gonna give you up\" buttons {\"OK\"} with title \"Rick Astley Says\" with icon 0'"
		os.system( self.commandStr )

		os.system( self.beepStr )
		self.commandStr = "osascript -e 'tell app \"System Events\" to display dialog \"Never gonna let you down\" buttons {\"OK\"} with title \"Rick Astley Says\" with icon 0'"
		os.system( self.commandStr )

		os.system( self.beepStr )
		self.commandStr = "osascript -e 'tell app \"System Events\" to display dialog \"Never gonna run around and desert you\" buttons {\"OK\"} with title \"Rick Astley Says\" with icon 0'"
		os.system( self.commandStr )

		os.system( self.beepStr )
		self.commandStr = "osascript -e 'tell app \"System Events\" to display dialog \"Never gonna make you cry\" buttons {\"OK\"} with title \"Rick Astley Says\" with icon 0'"
		os.system( self.commandStr )

		os.system( self.beepStr )
		self.commandStr = "osascript -e 'tell app \"System Events\" to display dialog \"Never gonna say goodbye\" buttons {\"OK I get it\"} with title \"Rick Astley Says\" with icon 0'"
		os.system( self.commandStr )

		os.system( self.beepStr )
		self.commandStr = "osascript -e 'tell app \"System Events\" to display dialog \"Never gonna tell a lie\" buttons {\"No really\"} with title \"Rick Astley Says\" with icon 0'"
		os.system( self.commandStr )

		os.system( self.beepStr )
		self.commandStr = "osascript -e 'tell app \"System Events\" to display dialog \"And hurt you\" buttons {\"Staaahp!\"} with title \"Rick Astley Says\" with icon 0'"
		os.system( self.commandStr )

		return

