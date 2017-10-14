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

class nmap_single_host_top_1000_and_probes( FireModule ):

	def __init__(self):
		self.commentsStr = "NetworkScans/nmap_single_host_top_1000_and_probes"
		return

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "NetworkScans/nmap_single_host_top_1000_and_probes"
		return

	def Description( self ):
		self.Description = "Runs nmap, probing Top 100 ports on target system, discovery against running services"
		return self.Description

        def Configure( self ):
                self.targetAddrStr = raw_input( "Enter Target System's IP Address (W.X.Y.Z) or domain name (SomeSite.com): " )
                return

        def GetParameters( self ):
                return( self.targetAddrStr )

        def SetParameters( self, parametersStr ):
                self.targetAddrStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print self.commentsStr + ": Setting Logging flag!"
                print logFlag
                return

        def Ignite( self ):
                if ( self.targetAddrStr == "" ):
                        print "## ", self.commentsStr, ": Error - Network address string is blank"
                        return
		else:
			self.commandStr = "nmap -Pn -n --open -sT -sV " + self.targetAddrStr
			print self.commentsStr + ": Scanning with " + self.commandStr
			os.system( self.commandStr )

		return

