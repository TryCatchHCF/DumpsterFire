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

import os, sys, urllib, random, string

from FireModules.fire_module_base_class import *

class create_500000_files( FireModule ):

	def __init__(self):
		self.commentsStr = "Filesystem/create_500000_files"
		self.mTargetDirectory = "/"
		self.fileNameBaseStr = ".us-west-2.elb.amazonaws.com"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Filesystem/create_500000_files"
		self.mTargetDirectory = "/"
		self.fileNameBaseStr = ".us-west-2.elb.amazonaws.com"
		return;

	def Description( self ):
		self.Description = "Creates 500,000 files named 'nomnomX' where X is the file number, writes 'nomnom' into each." 
		return self.Description

	def Configure( self ):
		self.mTargetDirectory = raw_input( "Enter target directory (Ex. /tmp/): " )
		return

	def GetParameters( self ):
		return self.mTargetDirectory

	def SetParameters( self, parametersStr ):
		self.mTargetDirectory = parametersStr
		return

	def ActivateLogging( self, logFlag ):
		print self.commentsStr + ": Setting Logging flag!"
		print logFlag
		return


	def Ignite( self ):

		print self.commentsStr + ": Creating 500,000 nomnom files in: " + self.mTargetDirectory

		# First we create files filled with 16MB of random trash, and continue until the target
		# directory/partition can't fit another 16MB file. Then repeat process with 1MB and 1KB
		# files in order to fill in the last nooks and crannies of all available space.

		i = 0
		self.sourceFilenameStr = ""

		try:
			while( i < 500000 ):

				self.sourceFilenameStr = self.mTargetDirectory + "nomnom" + str( i )

				self.file = open( self.sourceFilenameStr, "w")

				# Write kBytes * 1024 of random data to file
				self.file.write( 'nomnom' )
				self.file.close()

				i = i + 1

		except:
			# Exit when we can no longer create a file of the desired size in target directory
			print "Error creating nomnom file", self.sourceFilenameStr
			return

		return
		
