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

class download_custom_url( FireModule ):

	def __init__(self):
		self.commentsStr = "FileDownloads/download_custom_url"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "FileDownloads/download_custom_url"
		return;

	def Description( self ):
		self.Description = "Downloads user-supplied URL into current working directory"
		return self.Description

	def Configure( self ):
		self.mURL = raw_input( "Enter URL of file to download: " )
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

		print self.commentsStr + ": Downloading: " + self.mURL
		urllib.urlretrieve( self.mURL, 'download.file' )

		return

