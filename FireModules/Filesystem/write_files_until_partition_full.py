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

class write_files_until_partition_full( FireModule ):

	def __init__(self):
		self.commentsStr = "Filesystem/write_files_until_partition_full"
		self.mTargetDirectory = "/"
		self.fileNameBaseStr = ".us-west-2.elb.amazonaws.com"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Filesystem/write_files_until_partition_full"
		self.mTargetDirectory = "/"
		self.fileNameBaseStr = ".us-west-2.elb.amazonaws.com"
		return;

	def Description( self ):
		self.Description = "Creates AWS ELB cache-like files into the target directory until the partition is full. Files are filled with random data."
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

		print self.commentsStr + ": Writing out endless", self.fileNameBaseStr, "files to: " + self.mTargetDirectory

		# First we create files filled with 16MB of random trash, and continue until the target
		# directory/partition can't fit another 16MB file. Then repeat process with 1MB and 1KB
		# files in order to fill in the last nooks and crannies of all available space.

		self.mSixteenMB = 1024 * 16

		self.NomNom( self.mSixteenMB )
		self.NomNom( 1024 )
		self.NomNom( 1 )

		return


	def NomNom( self, kBytes ):

		# Keep looping until the file write fails. Ignite() will then call NomNom() with successively
		# smaller file sizes to fill up those smaller remaining partition spaces

		try:
			while( True ):

				self.sourceFilename = self.mTargetDirectory + self.GenerateFilename()

				print "Creating:", self.sourceFilename

				self.file = open( self.sourceFilename, "w")

				# Write kBytes * 1024 of random data to file
				self.file.write( ''.join([ random.choice( string.ascii_letters + string.digits ) for n in xrange( kBytes * 1024 )]))
				self.file.close()

		except:
			# Exit when we can no longer create a file of the desired size in target directory
			print "Error creating file", self.sourceFilename, ", should mean partition is filling up."
			return

		return
		

	def GenerateFilename( self ):

		try:
			# Generate a random string for the unique filename
			self.mFilename = ''.join([ random.choice( string.ascii_letters + string.digits ) for n in xrange( 24 )])

			# Merge the two
			self.mFilename = self.mFilename + self.fileNameBaseStr
		except:
			return( "error" + self.fileNameBaseStr )

		return( self.mFilename )
