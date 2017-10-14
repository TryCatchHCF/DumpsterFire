#!/usr/bin/python
# 
# Filename:  igniteDumsterFire.py 
#
# Version: 1.0.0
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:  
#
#	Takes name of DumpsterFire, loads associated settings file, proceeds to
#	execute component Fires. If time delay trigger has been set, will idle
#	until target time arrives. Executes each Fire module in sequence, starting
#	the next Fire once the previous Fire has exited. Checks for time delta
#	triggers for each Fire, delays execution as configured.
#
# Description:  
#
# 	Each DumpsterFire includes one or more DumpsterFire Elements
#
# Example:  
#
#   $ ./igniteDumpsterFire.py 
# 

import os, sys, getopt, dumpsterFireFactory

def IgniteDumpsterFireHeadless( dumpsterFireName ):

	# Load the named Dumpster Fire
	hotDumpsterFire = dumpsterFireFactory.LoadDumpsterFireConfig( dumpsterFireName )

	dumpsterFireFactory.IgniteDumpsterFire( hotDumpsterFire, hotDumpsterFire.mLaunchDateTimeUTC, False )

	return



if __name__ == "__main__":
	if ( len(sys.argv) != 2 ):
		print ""
		print "usage: igniteDumpsterFire.py <DumpsterFireFilePath>"
		print ""
		print "Example: ./igniteDumpsterFire.py my_dumpsterfire.fyr"
		print ""

		exit

	else:
		IgniteDumpsterFireHeadless( sys.argv[ 1 ])

