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

class download_tor_browser_windows( FireModule ):

	def __init__(self):
		self.commentsStr = "FileDownloads/download_tor_browser_windows"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "FileDownloads/download_tor_browser_windows"
		return;

	def Description( self ):
		self.Description = "Download Tor Browser for Windows"
		return self.Description

	def Configure( self ):
		self.mDirectoryPath = raw_input( "Enter Directory Path to download files into: " )
		return

	def GetParameters( self ):
		return self.mDirectoryPath

	def SetParameters( self, parametersStr ):
		self.mDirectoryPath = parametersStr
		return

	def ActivateLogging( self, logFlag ):
		print self.commentsStr + ": Setting Logging flag!"
		print logFlag
		return

	def Ignite( self ):

		self.filepath = self.mDirectoryPath + "/" + 'torbrowser-install.exe'
		print self.commentsStr + ": Downloading Tor Browser to: " + self.filepath
		urllib.urlretrieve( 'https://www.torproject.org/dist/torbrowser/7.0.6/torbrowser-install-7.0.6_en-US.exe', self.filepath )

		return
