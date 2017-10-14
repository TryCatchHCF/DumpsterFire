#!/usr/bin/python
#
# Filename:  testFireModule.py
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
#   $ ./testFireModule.py <FireModuleName.py>
#

import os, sys, getopt, datetime, random, importlib, json

# DEBUG DEBUG DEBUG - Replace with proper inclusion of classes so we don't
# have hardcoded duplicate class declarations

class FireNode:
        mFireName = ""
        mOffsetHours = 0
        mOffsetMinutes = 0
        mConfigStr = ""


class DumpsterFire:
        mName = ""
        mDescription = ""
        mFires = []      # List of FireNodes
        mDelayLaunch = 0
        mLaunchDateTimeUTC = datetime.datetime.utcnow() # If delayed launch selected, use this
        # FLAWED - CHANGE TO DERIVE LOCAL TIME DIRECTLY FROM mLaunchDateTimeUTC TO AVOID EDGE CASES
        mLaunchDateTimeLocal = datetime.datetime.now()  # If delayed launch selected, use this




# ================================================================================================
#
# Function:
#
# Description:
#
# ================================================================================================

def DebugTestFireTemplateMethods( modulePath, fireName ):

        print ""
        print "-------------------------------------------------"
        print "=============  Test Fire Module  ================"
        print "-------------------------------------------------"
        print ""
        print "Module Path:", modulePath
        print "Fire Name:", fireName
	print ""

	print "---------- Trying to locate Fire in module path... ----------"
	print ""	
        currentFireClass = getattr( importlib.import_module( modulePath, fireName ), fireName )
        thisFire = currentFireClass( "" )

	print "---------- Calling Configure() method ----------"
	print ""
        thisFire.Configure()
        print ""

	print "---------- Calling Description() method ----------"
	print ""
        print "\t Description: ", thisFire.Description()
        print ""

	print "---------- Calling GetParameters() method ----------"
	print ""
        parameters = thisFire.GetParameters()
	print "Fire parameters: ", parameters
        print ""

	print "---------- Calling SetParameters() method ----------"
	print ""
	print "Setting Fire parameters: ", parameters
        thisFire.SetParameters( parameters )
        print ""

	print "---------- Calling ActivateLogging() method ----------"
	print ""
        thisFire.ActivateLogging( True )
        print ""

	print "---------- Calling Ignite() method ----------"
	print ""
        thisFire.Ignite()
	print ""

	print "DONE!"
	print ""

        return


if __name__ == "__main__":
	if ( len(sys.argv) != 3 ):
		print ""
		print "usage: testFireModule.py <fireModulePath> <fireModuleName>>"
		print ""
		print "Example: ./testFireModule.py FireModules.Websurfing.warez_sites warez_sites"
		print ""
		exit

	else:
		DebugTestFireTemplateMethods( sys.argv[1], sys.argv[2] )

