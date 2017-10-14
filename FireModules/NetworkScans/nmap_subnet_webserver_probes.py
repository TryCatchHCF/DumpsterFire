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
#
# Description:
#
#
# Example:
#
#

import os, sys

from FireModules.fire_module_base_class import *

class nmap_subnet_webserver_probes( FireModule ):

	def __init__(self):
		self.commentsStr = "NetworkScans/nmap_subnet_webserver_probes"
		return

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "NetworkScans/nmap_subnet_webserver_probes"
		return

	def Description( self ):
		self.Description = "Runs nmap, probing common Webserver ports on target network, discovery against running Webservers"
		return self.Description

        def Configure( self ):
                self.networkAddrStr = raw_input( "Enter Target Network IP Address (W.X.Y.Z): " )
                return

        def GetParameters( self ):
                return( self.networkAddrStr )

        def SetParameters( self, parametersStr ):
                self.networkAddrStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):
                if ( self.networkAddrStr == "" ):
                        print "## ", self.commentsStr, ": Error - Network address string is blank"
                        return
		else:
			self.commandStr = "nmap -Pn -n --open -sT -sV -p80,443,8080,8443 --script=http-enum " + self.networkAddrStr + "/24" 
			print self.commentsStr + ": Scanning with " + self.commandStr
			os.system( self.commandStr )

		return

