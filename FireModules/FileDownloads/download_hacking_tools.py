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

class download_hacking_tools( FireModule ):

	def __init__(self):
		self.commentsStr = "FileDownloads/download_hacking_tools"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "FileDownloads/download_hacking_tools"
		return;

	def Description( self ):
		self.Description = "Downloads various hacking tools to local directory"
		return self.Description

	def Configure( self ):
		self.mDirectoryPath = raw_input( "Enter Directory Path to download files into: " )
		return

	def GetParameters( self ):
		return self.mDirectoryPath

	def SetParameters( self, parametersStr ):
		self.mDirectoryPath =  parametersStr

		# Add a trailing "/" if they left it off (on Windows, Python will convert "/" to "\" for us)
		if not ( self.mDirectoryPath.endswith( '/' )):
			self.mDirectoryPath = self.mDirectoryPath + "/"
		return

	def ActivateLogging( self, logFlag ):
		print self.commentsStr + ": Setting Logging flag!"
		print logFlag
		return

	def Ignite( self ):

		self.filepath = self.mDirectoryPath + 'mimikatz.zip'
		print self.commentsStr + ": Downloading Mimikatz to: " + self.filepath
		urllib.urlretrieve( 'https://github.com/gentilkiwi/mimikatz/archive/master.zip', self.filepath )

		self.filepath = self.mDirectoryPath + 'responder.zip'
		print self.commentsStr + ": Downloading Responder to: " + self.filepath
		urllib.urlretrieve( 'https://github.com/SpiderLabs/Responder/archive/master.zip', self.filepath )

		self.filepath = self.mDirectoryPath + 'scapy.zip'
		print self.commentsStr + ": Downloading Scapy to: " + self.filepath
		urllib.urlretrieve( 'https://github.com/secdev/scapy/archive/v2.3.2.zip', self.filepath )

		self.filepath = self.mDirectoryPath + 'sqlmap.zip'
		print self.commentsStr + ": Downloading SQLMap to: " + self.filepath
		urllib.urlretrieve( 'https://github.com/sqlmapproject/sqlmap/archive/master.zip', self.filepath )

		self.filepath = self.mDirectoryPath + 'default-passwords.csv'
		print self.commentsStr + ": Downloading default passwords list to: " + self.filepath
		urllib.urlretrieve( 'https://github.com/danielmiessler/SecLists/blob/master/Passwords/default-passwords.csv', self.filepath )

		self.filepath = self.mDirectoryPath + '10k_most_common.txt'
		print self.commentsStr + ": Downloading 10K common passwords to: " + self.filepath
		urllib.urlretrieve( 'https://github.com/danielmiessler/SecLists/blob/master/Passwords/10k_most_common.txt', self.filepath )

		return
