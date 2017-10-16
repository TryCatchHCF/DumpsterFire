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
# Description:
#
#
# Example:
#
#

import os, sys

from FireModules.fire_module_base_class import *

class csh_aliases_fake_filesystem_errors( FireModule ):

	def __init__(self):
		self.commentsStr = "Shenanigans/csh_aliases_fake_filesystem_errors"
		self.cshFilePathStr = ""

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Shenanigans/csh_aliases_fake_filesystem_errors"
		self.cshFilePathStr = ""
		return;

	def Description( self ):
		self.Description = "Appends a series of aliases to the supplied csh resource file, printing system error messages when attempting to use commands such as 'ls', 'cd', 'df', etc. NOTE: Changing the global csh resource file requires root privileges."
		return self.Description

        def Configure( self ):
                self.cshFilePathStr = raw_input( "Filepath to csh resource file: " )
                return

        def GetParameters( self ):
                return( self.cshFilePathStr )

        def SetParameters( self, parametersStr ):
                self.cshFilePathStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

                if ( self.cshFilePathStr == "" ):
                        print "## ", self.commentsStr, ": Error - Bash filepath string is blank"
                        return

		else:
			# Unlike bash, csh often won't let you set an alias for "alias" or "unalias", so we'll skip those

			self.commandStr = "echo \"alias ls 'echo \"Directory not available\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias mv 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias cat 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias vi 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias vim 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias view 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias emacs 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias ed 'echo \"Error opening stdin\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias sed 'echo \"Error opening stdin\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias cp 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias rm 'echo \"File not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias cd 'echo \"Directory not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias pwd 'echo \"Directory not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias df 'echo \"Error accessing filesystem\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias du 'echo \"Error accessing filesystem\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias who 'echo \"Error accessing filesystem\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias ps 'echo \"Error accessing active process list\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias last 'echo \"Error accessing filesystem\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias fsck 'echo \"Filesystem corrupted, could not find entry point \"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias mount 'echo \"Error mounting node, filesystem tree not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias umount 'echo \"Error unmounting node, filesystem tree not found\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

			self.commandStr = "echo \"alias alias 'echo \"la=\'ls -a\'\"'\" >> " + self.cshFilePathStr
			print self.commentsStr + ": Running ==>", self.commandStr
			os.system( self.commandStr )

		return

