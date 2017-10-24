#!/usr/bin/python
#
# Filename:  testFireModule.py
#
# Version: 1.0.1
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:
#
#	Utility script for debugging Fire modules. Executes each member method
#	of the target Fire class, giving direct visibility into its operations
#	prior to using it in dumpsterFireFactory's menu-driven environment.
#
# Description:
#
#	The script takes two arguments - the full filepath of the Fire (in
#	Python package format - see example below), and the name of the Fire
#	class (note the lack of the .py suffix).
#
# Example:
#
#   $ ./testFireModule.py FireModules/Websurfing/warez_sites.py
#

import os, sys, getopt, importlib, dumpsterFireFactory



# ================================================================================================
#
# Function:  DebugTestFireTemplateMethods()
#
# Description:  Loads the Fire class from the module path (in Python package format)
# then calls each of the Fire's member methods. Does not use any exception handling
# so that you can see the direct location and cause of any errors.
#
# ================================================================================================

def DebugTestFireTemplateMethods( fireFilepathStr ):

	# Strip trailing ".py" suffix from filepath so we can convert to Python package format
	fireFilepathStr = fireFilepathStr[ :-3 ]

	# Convert filepath to Pythong package format
	firePackagePathStr = fireFilepathStr.replace( '/', '.' )	

	# Break down that package path into its components so we can grab the Fire name
	fireElementList = firePackagePathStr.split( "." )

	# Extract Fire name
	fireNameStr = fireElementList[ -1 ]

        print ""
        print "-------------------------------------------------"
        print "=============  Test Fire Module  ================"
        print "-------------------------------------------------"
        print ""
        print "Module Path:", firePackagePathStr
        print "Fire Name:", fireNameStr
	print ""

	print "---------- Trying to locate Fire in module path... ----------"
	print ""	
        currentFireClass = getattr( importlib.import_module( firePackagePathStr, fireNameStr ), fireNameStr )
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
	if ( len(sys.argv) != 2 ):
		print ""
		print "usage: testFireModule.py <filePathToFire>"
		print ""
		print "Example: ./testFireModule.py FireModules/Websurfing/warez_sites"
		print ""
		exit

	else:
		DebugTestFireTemplateMethods( sys.argv[1] )

