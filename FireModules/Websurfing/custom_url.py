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

class custom_url( FireModule ):

	def __init__(self):
		self.commentsStr = "Websurfing/custom_url"

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "Websurfing/custom_url"
		return;

	def Description( self ):
		self.Description = "Opens a Web connection to the supplied URL"
		return self.Description

        def Configure( self ):
                self.customUrlStr = raw_input( "Enter URL: " )
                return

        def GetParameters( self ):
                return( self.customUrlStr )

        def SetParameters( self, parametersStr ):
                self.customUrlStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):

                if ( self.customUrlStr == "" ):
                        print "## ", self.commentsStr, ": Error - URL is blank"
                        return

		else:
			print self.commentsStr + ": Opening connection to URL => " + self.customUrlStr
			self.webSession = urllib.urlopen( self.customUrlStr )
			trash = self.webSession.read()	

		return

