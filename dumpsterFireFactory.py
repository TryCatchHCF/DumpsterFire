#!/usr/bin/python
# 
# Filename:  dumpsterFireFactory.py 
#
# Version: 1.0.1
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:  
#
#	Create and execute time-delayed, distributed security incidents for Red- and Blue
#	Team exercises. Allows repeatable, trackable
#
#	User interface for creating, reviewing, editing, and executing DumpsterFires. 
#	Menu-driven with in-context help, walks the user through each step of the process.
#
# Description:  
#
#	dumpsterFire.py enters an event-driven menu loop, walking the user through all 
#	of the steps for creating, reviewing, editing, and igniting DumpsterFires. Help
#	files and a simple walk-through are available for the user to reference. Each
#	menu 
#
# 	Each DumpsterFire includes one or more Fire modules
#
#	To ignite an existing DumpsterFire in "headless" mode, use 'igniteDumpsterFire.py'
#	script located in the same directory.
#
# Example:  
#
#   $ ./dumpsterFireFactory.py 
# 

import os, sys, getopt, datetime, time, random, importlib, json, igniteDumpsterFire


# Each DumpsterFire includes one or more DumpsterFire Elements

class FireNode:
	mFireName = ""
	mOffsetHours = 0
	mOffsetMinutes = 0
	mConfigStr = ""


class DumpsterFire:
	mName = ""
	mDescription = ""
	mFires = []	 # List of FireNodes
	mDelayLaunch = False
	# Set default launch date to now, basically "Immediately", so we have a valid date initialized
	mLaunchDateTimeUTC = datetime.datetime.utcnow()	# Default to now, basically "Immediate"


kDumpsterFireDirectory = "DumpsterFires/"
kLabelDumpsterFireName = "Name:"
kLabelDumpsterFireDescription = "Description:"
kLabelDelayedIgnition = "Delayed Ignition:"
kLabelDelayedIgnitionStart = "Delayed Ignition Start:"
kLabelDelayedIgnitionStartUTC = "Delayed Ignition Start (UTC):"

# Used to filter out the required "__init__.py" files from displayed FireModule lists
kLabelDirInitFile = "__init__.py"

# Create lists of DumpsterFires, Fire Categories, and Fires 
# Global variables can be a source of trouble, and yet here I am...
# Used for menu-driven interaction while browsing DumpsterFires and Fires

gDumpsterFires = []
gFireCategories = []
gFires = []
gDumpsterFire = DumpsterFire

# Load the list of saved DumpsterFires
for root, dirs, files in os.walk( "./DumpsterFires" ):
	for file in files:
		if file.endswith('.fyr'):
			gDumpsterFires.append( file )
	    
# Load the list of available Fire Categories, basically any directory in "./FireModules/"
for root, dirnames, filenames in os.walk( "./FireModules" ):
	for dir in dirnames:
		gFireCategories.append( dir )
	    
# Lists of Fires are loaded based on user's selection of a Category, dynamically
# populates per Category



# ================================================================================================
#
# Function:  PrintBannerFlames()
#
# Description:  Print those little ASCII flames to give some visual flavor to menu-driven interfaces
#
# ================================================================================================

def PrintBannerFlames():

	print ""
	print "     (                                             (                 " 
	print "    )\ )                            )            )\ )                " 
	print "   (()/(                         ( /(   (   (   (()/(  (   (         " 
	print "    /(_)) (      )               )\()) ))\  )(   /(_)) )\  )(   (    "
	print "   (_))_ ))\    (     `  )   (  (_))/ /((_)(()\ (_))_|((_)(()\ ))\   "

	return



# ================================================================================================
#
# Function:  BuildDumpsterFire()
#
# Description:  High level method to that walks the user through the process of building
# DumpsterFires. Prints in-context help describing the process, then moves into the steps.
# See the printed context help below for a description of the workflow.
#
# ================================================================================================

def BuildDumpsterFire():

	newDumpsterFire = DumpsterFire()

	PrintBannerFlames()

	print ""
	print "---------------------------------------------------------------------"
	print "=====================   Build a Dumpster Fire   ====================="
	print "---------------------------------------------------------------------"
	print ""
	print "Recipe:"
	print ""
	print "     - Build a list of Fires, in the desired order of execution"
	print "     	+ Select a Fire Category"
	print "     	+ Review and Select a Fire from Category"
	print "     	+ Repeat until list is complete"
	print "     - Review list of selected Fires"
	print "     - Configure the Fires"
	print "     	+ Fires that have configuration options will prompt you for input"
	print "     - Choose timing of sequential Fire execution: Immediate or Relative Offset"
	print "     	+ Immediate: Each Fire starts immediately after previous Fire completes"
	print "     	+ Relative Offset: Fire delays for [hours:minutes] after previous Fire completes"
	print "     		* Assign separate Relative Offset for each Fire in your Dumpster Fire"
	print "     - Review Dumpster Fire"
	print "     - Save new Dumpster Fire for future use"
	print ""

	newDumpsterFire.mName = "Unnamed"

	AddFires( newDumpsterFire )

	print ""
	choice = raw_input("Continue building this Dumpster Fire? [y/n]: ")

	if choice == "y":

		print ""
		ConfigureDumpsterFire( newDumpsterFire )

		print ""
		PrintDumpsterFireConfig( newDumpsterFire )

		print "" 
		print "" 
		choice = raw_input("Save this Dumpster Fire? [y/n]: ")
	
		if choice == "y":

			SaveDumpsterFire( newDumpsterFire )
			gDumpsterFire = newDumpsterFire

		print ""

	# Delete the allocated DumpsterFire, else things get cluttered between iterations
	del newDumpsterFire.mFires[ : ]
	del newDumpsterFire

	return



# ================================================================================================
#
# Function:  ConfigureExistingDumpsterFire()
#
# Description:  Prompts user to select a saved DumpsterFire, then walks them through the process
# of updating its configuration.
#
# ================================================================================================

def ConfigureExistingDumpsterFire():

	selection = SelectDumpsterFire()
	print ""

	if ( selection > -1 ):

		thisDumpsterFire = LoadDumpsterFireConfig( kDumpsterFireDirectory + gDumpsterFires[ selection ] )
	
		ConfigureDumpsterFire( thisDumpsterFire )

		PrintDumpsterFireConfig( thisDumpsterFire )

		print ""
		print "Storing Dumpster Fire..."
		SaveDumpsterFire( thisDumpsterFire )
		print ""

		# Free up the allocated space or gets mucked up from repeated calls to this method
		del thisDumpsterFire.mFires[ : ]
		del thisDumpsterFire
	return



# ================================================================================================
#
# Function:  ConfigureDumpsterFire()
#
# Description:  Loops through the provided DumpsterFire's list of Fire modules. 
#
# First creates the Python package name that leads to the current Fire module. Next, loads 
# the matching Fire class and its own Configuration() method, which prompts the user for any 
# needed config settings.
#
# ================================================================================================

def ConfigureDumpsterFire( thisDumpsterFire ):

	# Edit DumpsterFire Time Delay
	# TO DO - TO DO - TO DO
	# DEBUG DEBUG DEBUG

	print "====  Configure DumpsterFire  ===="
	print ""

	# Loop over Fires
	#	Create Python package name from Fire name
	#	Load matching Fire and its classes
	#	Call Fire's Configure() method

	i = 0

	while ( i < len( thisDumpsterFire.mFires )):

		currentFire = thisDumpsterFire.mFires[ i ]

		print "---------------------------------------------------------"
		print ""
		print "Current Fire: ", currentFire.mFireName
		print ""

		# Convert Fire's filepath to Python package '.'-format

		pythFormatPathStr = currentFire.mFireName.replace( "/", "." )

		# Set root path to Fire modules, strip trailing ".py" from Fire module's name

		fireModulePathStr = "FireModules." + pythFormatPathStr[ :-3 ]

		# Extract Fire name from end of converted Fire module path 
		# Convert filepath of Fire module to Python's '.'-notation

		fireModulePathElementList = fireModulePathStr.split( "." )
		fireModuleNameStr = fireModulePathElementList[ -1 ] 

		try:
			# Load Fire module (Python class)
			currentFireClass = getattr( importlib.import_module( fireModulePathStr, fireModuleNameStr ), fireModuleNameStr )

			# Create instance of Fire, with parameters that were stored in parent DumpsterFire
			thisFire = currentFireClass( "" )

			try:
				thisFire.Configure() 
				currentFire.mConfigStr = thisFire.GetParameters()

			except:
				print "### Error while running Fire's Configure() method"

		except:
			print "### ConfigureDumpsterFire(): Error loading fire."
			print "Module Path:", fireModulePathStr
			print "Fire Name:", fireModuleNameStr

		i = i + 1

	currentDT_UTC = datetime.datetime.utcnow()

	print ""
	print "-----------------  DumpsterFire Name  -----------------"
	print ""
	print "NOTE: DumpsterFire names must only contain letters, numbers, hyphens, and underscores"
	print ""
	thisDumpsterFire.mName = raw_input( "Enter name for new Dumpster Fire: " )
	print ""

	print "--------------  DumpsterFire Time Delay  --------------"
	print ""
	print "DumpsterFire Time Delay (UTC):", thisDumpsterFire.mLaunchDateTimeUTC.strftime( "%x %X" )
	print "Current Time (UTC):", currentDT_UTC.strftime("%x %X")
	print ""
	choice = raw_input( "Create new time-delay for dumpster fire? [y/n]: ")

	if choice == "y":
		
		thisDumpsterFire.mLaunchDateTimeUTC = BuildDateTime()
		thisDumpsterFire.mDelayLaunch = True

	return



# ================================================================================================
#
# Function:  AddFires()
#
# Description:  Prompts the user through browsing the Fire Categories and selecting Fires from
# each, building a list of Fires to the current DumpsterFire 
#
# ================================================================================================

def AddFires( thisDumpsterFire ):

	done = False
	fireCount = 0

	# Empty out and Fires that may be left over from previous ops
	del thisDumpsterFire.mFires[ : ]

	while not done:

		print ""
		print "====  Select a Fire Category  ===="
		print ""

		fireCategoryNum = SelectFireCategory()
		fireCategory = gFireCategories[ fireCategoryNum ]

		print "Selected Fire Category: ", fireCategory

		print ""
		print "====  Select a Fire ===="
		print ""

		fireNum = SelectFire( fireCategory )
	    
		thisDumpsterFire.mFires.append( FireNode() )
		thisDumpsterFire.mFires[ fireCount ].mFireName = fireCategory + "/" + gFires[ fireNum ]

		fireCount = fireCount + 1

		choice = raw_input("Add another Fire? [y/n]: ")

		if not ( choice == "y" ):
			done = True

	ReviewFires( thisDumpsterFire )

	print ""
	choice = raw_input("Add time offsets to each Fire? [y/n]: ")
	print ""

	if choice == "y":
		thisDumpsterFire = AddTimeOffsetsToFires( thisDumpsterFire )

	return ( thisDumpsterFire )



# ================================================================================================
#
# Function:  ReviewFires()
#
# Description:  Just prints of list of Fire names in the given DumpsterFire, used to check
# progress while building a new DumpsterFire
#
# ================================================================================================

def ReviewFires( thisDumpsterFire ):

	print ""
	print "====  Review Dumpster Fire  ===="
	print ""
	print "Selected Fires (in order of execution):"
	print ""

	i = 0

	while ( i < len( thisDumpsterFire.mFires )):
		print "\t", thisDumpsterFire.mFires[ i ].mFireName
		i = i+1

	return



# ================================================================================================
#
# Function:  AddTimeOffsetsToFires
#
# Description:  Adds a relative offset time delay to wait before igniting the associated Fire.
# Useful for building more believable event narratives with a DumpsterFire. When the previous
# Fire in the queue finishes running, the Fire will wait HH:MM before igniting itself.
#
# ================================================================================================

def AddTimeOffsetsToFires( thisDumpsterFire ):

	print ""
	print "=======  Add Time Offsets To Fires  ======="
	print ""
	print "Select time offsets for each Fire"
	print ""

	done = 0
	i = 0

	while ( i < len( thisDumpsterFire.mFires )):

		while ( done == 0 ):

			thisDumpsterFire.mFires[ i ] = BuildTimeOffsetForFire( thisDumpsterFire.mFires[ i ] )
			keepTimeOffset = raw_input( "Keep time offset? (y/n): " )
	
			if ( keepTimeOffset == "y" ):
				done = 1
			else:
				thisDumpsterFire.mFires[ i ].mOffsetHours = 0
				thisDumpsterFire.mFires[ i ].mOffsetMinutes = 0

		done = 0
		i = i+1

	return( thisDumpsterFire )


# ================================================================================================
#
# Function:  BuildTimeOffsetForFire()
#
# Description:  Helper function for AddTimeOffsetsToFires()
#
# ================================================================================================

def BuildTimeOffsetForFire( thisFire ):

	hour = 0
	minute = 0

	print "Assigning time offset for Fire: ", thisFire.mFireName
	print ""

	done = 0

	while ( done == 0 ):
                try:
                        hours = int ( raw_input( "Enter Hour (0-23): " ))

                        if ( hours < 0 or hours > 23 ):
                                print "Invalid hour, try again..."
			else:
				done = 1

                except ValueError:
                        print "Invalid hour, try again..."
	done = 0

	while ( done == 0 ):
                try:
                        minutes = int ( raw_input( "Enter Minutes (0-59): " ))

                        if ( minutes < 0 or minutes > 59 ):
                                print "Invalid minutes, try again..."
			else:
				done = 1

                except ValueError:
                        print "Invalid minutes, try again..."

	print ""
	print "Time offset for Fire '" + thisFire.mFireName + "': ",  \
		str( hours ).zfill( 2 ), "hours,", str( minutes ).zfill( 2 ), "minutes"
	print ""

	thisFire.mOffsetHours = hours
	thisFire.mOffsetMinutes = minutes

        return( thisFire )



# ================================================================================================
#
# Function:  BrowseFires()
#
# Description:  Guides the user through selecting Fire Categories, prints the included
# Fires (and their respective descriptions) for an overview.
#
# ================================================================================================

def BrowseFires():

	PrintBannerFlames()

	print "---------------------------------------------------------------------"
	print "=========================   BROWSE FIRES   =========================="
	print "---------------------------------------------------------------------"
	print ""
	print "Fires are the individual action elements that make up a Dumpster Fire."
	print ""
	print "Select a Fire Category to view its member Fires and their descriptions."
	print ""

	done = 0

	while ( done == False ):

		print ""
		print "====  Select a Fire Category  ===="
		print ""

		fireCategoryNum = SelectFireCategory()
		fireCategory = gFireCategories[ fireCategoryNum ]

		print "Selected Fire Category: ", fireCategory

		print ""
		PrintBannerFlames()

		print "---------------------------------------------------------------------"
		print "                 ", fireCategory, "Fire Details"
		print "---------------------------------------------------------------------"
		print ""

		# Clear values from list to avoid duplicate crud building up
		del gFires[ : ]

		# Populate the Fire modules from the supplied Fire Category
		for root, dirs, files in os.walk( "./FireModules/" + fireCategory ):
			for file in files:
				# Filter out the required __init__.py file in Fire directories
				if ( file != kLabelDirInitFile ):
					if file.endswith('.py'):
						gFires.append( file )

		i = 0

		while i < len( gFires ):

			PrintFireDetails( fireCategory, gFires[ i ] )
			i = i + 1
	    
		choice = raw_input("Browse more Fires? [y/n]: ")

		if not ( choice == "y" ):
			done = True

	return 



# ================================================================================================
#
# Function:  PrintFireDetails()
#
# Description:  Utility function for printing the details of a Fire (name, configuration,
# and time delays) in a friendly layout that won't make the user's eyes burn.
#
# ================================================================================================

def PrintFireDetails( fireCategory, fireName ):

	try:
		fullFirePath = fireCategory + "/" + fireName

		# Convert Fire's filepath to Python '.'-format
		pythFormatPathStr = fullFirePath.replace( "/", "." )

		# Set root path to Fire modules, strip trailing ".py" from Fire module's name
		fireModulePathStr = "FireModules." + pythFormatPathStr[ :-3 ]

		# Extract Fire name from end of converted Fire module path 
		# Convert filepath of Fire module to Python's '.'-notation

		fireModulePathElementList = fireModulePathStr.split( "." )
		fireModuleNameStr = fireModulePathElementList[ -1 ] 

	except:
		print "### PrintFireDetails(): Error accessing Fire details for", fireModuleNameStr
		print ""

	try:
		# Load Fire module (Python class)
		currentFireClass = getattr( importlib.import_module( fireModulePathStr, fireModuleNameStr ), fireModuleNameStr )

		# Create dummy instance of Fire so we can call its Description() method
		thisFire = currentFireClass( "" )

	except:
		print "### PrintFireDetails(): Error loading / creating new Fire" 
		print "Module Path:", fireModulePathStr
		print "Fire Name:", fireModuleNameStr
		print ""

	try:
		print "**", fireName
		print ""
		print "\t", thisFire.Description()
		print ""

	except:
		print "### IgniteFire: Error while calling Fire's Description()"
		print ""

	
	return



# ================================================================================================
#
# Function:  StoreDumpsterFireConfig()
#
# Description:  Creates a JSON-format snapshot of the DumpsterFire, saves to "DumpsterFires/"
# directory.
#
# ================================================================================================

def StoreDumpsterFireConfig( theDumpsterFire ):

	# Store theDumpsterFire in JSON format in our DumpsterFires/ directory

	rawConfigList = []

	try:
		configFile = open( "DumpsterFires/" + theDumpsterFire.mName + ".fyr", 'w' )

	except:
		print "Error opening config file DumpsterFires/" + theDumpsterFire.mName + ".fyr"
		print ""

	try:
		rawConfigList.append( theDumpsterFire.mName )
		rawConfigList.append( theDumpsterFire.mDescription )
		rawConfigList.append( theDumpsterFire.mLaunchDateTimeUTC.strftime("%m/%d/%Y %H:%M:00"))
		rawConfigList.append( theDumpsterFire.mDelayLaunch )
		rawConfigList.append( len( theDumpsterFire.mFires ))
		
		# Launch Date/Time are not stored in the config file - those are runtime settings
		#
		# Onward to storing the member Fires and their settings...

		i = 0

		while i < len( theDumpsterFire.mFires ):

			fire = theDumpsterFire.mFires[ i ]

			rawConfigList.append( fire.mFireName )
			rawConfigList.append( fire.mOffsetHours )
			rawConfigList.append( fire.mOffsetMinutes )
			rawConfigList.append( fire.mConfigStr )
		
			i = i + 1

		json.dump( rawConfigList, configFile )

	except:
		print "Error streaming JSON to config file."
		print ""

	try:
		configFile.close()

	except:
		print "Error closing config file."
		print ""

	return



# ================================================================================================
#
# Function:  LoadDumpsterFireConfig()
#
# Description:  Reads in the JSON-format saved DumpsterFire file, creates a new DumpsterFire
# object and populates it with the saved values.
#
# ================================================================================================

def LoadDumpsterFireConfig( dumpsterFireFilePath ):

	# Open DumpsterFire config file 
	# Read saved JSON format and assign values to data members

	newDumpsterFire = DumpsterFire()
	rawConfigStr = []

	try:
		configFile = open( dumpsterFireFilePath, 'r' )

	except:
		print "Error opening config file " + dumpsterFireFilePath
		print ""

	# Some ugly brittleness ahead - hardcoded indexing of fields. Won't cause any
	# problems unless you start modifying the number of fields that are stored
	# when saving/loading DumpsterFires

	try:
		# Load raw config strings into list, assign them to DumpsterFire members
		rawConfigStr = json.load( configFile )

		newDumpsterFire.mName = rawConfigStr[ 0 ]
		newDumpsterFire.mDescription = rawConfigStr[ 1 ]
		newDumpsterFire.mLaunchDateTimeUTC = datetime.datetime.strptime( rawConfigStr[ 2 ], "%m/%d/%Y %H:%M:%S" )
		newDumpsterFire.mDelayLaunch = rawConfigStr[ 3 ]


		fireCount = rawConfigStr[ 4 ]

		i = 0

		while i < fireCount:
			
			newDumpsterFire.mFires.append( FireNode() )

			offset = i * 4

			newDumpsterFire.mFires[ i ].mFireName = rawConfigStr[ offset + 5 ]
			newDumpsterFire.mFires[ i ].mOffsetHours = rawConfigStr[ offset + 6 ]
			newDumpsterFire.mFires[ i ].mOffsetMinutes = rawConfigStr[ offset + 7 ]
			newDumpsterFire.mFires[ i ].mConfigStr = rawConfigStr[ offset + 8 ]

			i = i + 1

	except:
		print "Error reading values from config file."
		print ""

	try:
		configFile.close()

	except:
		print "Error closing config file."
		print ""

	return( newDumpsterFire )



# ================================================================================================
#
# Function:  SaveDumpsterFire()
#
# Description:  Helper function for storing DumpsterFires via StoreDumpsterFireConfig(). 
# First prints out the details so the user gets an overview of what they're storing.
#
# ================================================================================================

def SaveDumpsterFire( newDumpsterFire ):

	print ""
	newDumpsterFire.mDescription = raw_input( "Enter description of new Dumpster Fire: " )

	print ""
	print "** Saving new Dumpster Fire: "

	PrintDumpsterFireConfig( newDumpsterFire )

	StoreDumpsterFireConfig( newDumpsterFire )

	print ""
	print ""
	print "** Successfully saved:", newDumpsterFire.mName
	print ""
	choice = raw_input( "Press return to continue... " )

	return


# ================================================================================================
#
# Function:  PrintDumpsterFireConfig()
#
# Description:  Helper function, prints the DumpsterFire's configuration in a nice format.
#
# ================================================================================================

def PrintDumpsterFireConfig( thisDumpsterFire ):

	i = 0

	print ""
	print "\t", kLabelDumpsterFireName, thisDumpsterFire.mName
	print "\t", kLabelDumpsterFireDescription, thisDumpsterFire.mDescription

	if ( thisDumpsterFire.mDelayLaunch == False ):
		print "\t", kLabelDelayedIgnition, "No"

	else:
		print "\t", kLabelDelayedIgnition, "Yes"
		print "\t", kLabelDelayedIgnitionStartUTC, thisDumpsterFire.mLaunchDateTimeUTC.strftime("%x %X")

	print ""
	print "\tFires (In order of execution):"
	print ""

	while ( i < len( thisDumpsterFire.mFires )):
		print "\t** ", thisDumpsterFire.mFires[ i ].mFireName
		print "\t    Relative Time Delay (HH:MM): ",  \
			str( thisDumpsterFire.mFires[ i ].mOffsetHours ).zfill(2) + ":" +  \
			str( thisDumpsterFire.mFires[ i ].mOffsetMinutes ).zfill(2)
		print "\t    Config: " + thisDumpsterFire.mFires[ i ].mConfigStr
		i = i+1

	return



# ================================================================================================
#
# Function:  IgniteDumpsterFire()
#
# Description:  Where the good stuff happens.
#
# If DumpsterFire has fuse delay, loop and wait until triggered
# Loop over Fires in thisDumpsterFire
# For each Fire
# 	Parse each Fire name into FireModulePath and FireName
#		Convert FireModulePath + FireName into Python package format
#			(Replace '/' with '.' in path)
#		Copy fireName from last field of FireModulePath
#	Load Fire module
#	Set Configs for Fire
#	Check for Fire's delayed fuse, wait as needed
# 	Call IgniteFire() of Fire
# Exit
#
# ================================================================================================

def IgniteDumpsterFire( thisDumpsterFire, withUserInteraction ):

	i = 0

	# If this DumpsterFire has delayed ignition, loop and wait until triggered
	if ( thisDumpsterFire.mDelayLaunch == True ):

		print "Delayed ignition selected. Standing by until UTC", 
		print thisDumpsterFire.mLaunchDateTimeUTC.strftime("%x %X")
		print ""
	
		waitTime = thisDumpsterFire.mLaunchDateTimeUTC - datetime.datetime.utcnow()

		if ( waitTime.total_seconds() > 1 ):

			time.sleep( waitTime.total_seconds() )

		
	print "Igniting Dumpster Fire..."

	# Loop through the member Fires of the DumpsterFire, igniting them in turn

	while ( i < len( thisDumpsterFire.mFires )):

		currentFire = thisDumpsterFire.mFires[ i ]

		print ""
		print "---------------------------------------------------------"
		PrintDateTimeStamps()
		print ""

		# If this Fire has a relative delayed ignition, loop and wait until triggered
		if ( currentFire.mOffsetHours > 0 or currentFire.mOffsetMinutes > 0 ):

			print "Delayed Fire ignition detected. Pausing for (HH:MM)", \
				str( currentFire.mOffsetHours ).zfill(2) + ":" +  \
				str( currentFire.mOffsetMinutes ).zfill(2)
			print "(Waiting...)"
			
			delaySeconds = ( int(currentFire.mOffsetMinutes) * 60 ) + ( int(currentFire.mOffsetHours) * 60 * 60 )

			time.sleep( delaySeconds )
			print ""
			PrintDateTimeStamps()
			print ""

		print "Igniting Fire: ", currentFire.mFireName
		if ( currentFire.mConfigStr == "" ):
			print "Using ConfigStr: (None)"
		else:
			print "Using ConfigStr: ", currentFire.mConfigStr

		# Convert Fire's filepath to Python '.'-format
		pythFormatPathStr = currentFire.mFireName.replace( "/", "." )

		# Set root path to Fire modules, strip trailing ".py" from Fire module's name
		fireModulePathStr = "FireModules." + pythFormatPathStr[ :-3 ]

		# Extract Fire name from end of converted Fire module path 
		# Convert filepath of Fire module to Python's '.'-notation
		fireModulePathElementList = fireModulePathStr.split( "." )
		fireModuleNameStr = fireModulePathElementList[ -1 ] 

		# Time to ignite the current Fire...
		IgniteFire( fireModulePathStr, fireModuleNameStr, currentFire.mConfigStr )

		i = i+1

	print "---------------------------------------------------------"
	PrintDateTimeStamps()
	print ""
	print "All Fires burned. DumpsterFire complete."
	print ""

	return



# ================================================================================================
#
# Function:  StartDumpsterFire()
#
# Description: Sets up all of the housekeeping needed to ignite the DumpsterFire.
#
# ================================================================================================

def StartDumpsterFire():

	PrintBannerFlames()

	print ""
	print "---------------------------------------------------------------------"
	print "=====================   Start a Dumpster Fire   ====================="
	print ""
	print "Recipe:"
	print ""
	print "     - Select an available Dumpster Fire"
	print "     - Choose immediate ignition or time-delayed"
	print "     - Review Dumpster Fire settings"
	print "     - Ignite Dumpster Fire"
	print ""
	print ""
	print "---------------------------------"
	print "====  Select a Dumpster Fire ===="
	print ""

	selection = SelectDumpsterFire()

	if ( selection < 0 ):
		return

	hotDumpsterFire = LoadDumpsterFireConfig( kDumpsterFireDirectory + gDumpsterFires[ selection ] )

	print ""
	print ""
	print "---------------------------------"
	print "====  Select Timing of Fire  ===="
	print ""

	# DEBUG DEBUG DEBUG
	fuseDelayStr = hotDumpsterFire.mLaunchDateTimeUTC.strftime("%x %X")
	currentDT_UTC = datetime.datetime.utcnow()

	waitTime = hotDumpsterFire.mLaunchDateTimeUTC - datetime.datetime.utcnow()

	if ( waitTime.total_seconds() < 1 ):
		fuseDelayStr = "None (immediate ignition)"

	print "DumpsterFire Time Delay (UTC):", fuseDelayStr
	print "Current Time (UTC):", currentDT_UTC.strftime("%x %X")

	fuseDelayStr = hotDumpsterFire.mLaunchDateTimeUTC.strftime("%x %X")

	print ""
	choice = raw_input( "Create new time-delay for dumpster fire? [y/n]: ")
	print ""

	if choice == "y":
		
		hotDumpsterFire.mLaunchDateTimeUTC = BuildDateTime()
		fuseDelayStr = hotDumpsterFire.mLaunchDateTimeUTC.strftime("%x %X")
		hotDumpsterFire.mDelayLaunch = True

	elif ( waitTime.total_seconds() < 1 ):

		fuseDelayStr = "None (immediate ignition)"
		hotDumpsterFire.mDelayLaunch = False

	print ""
	print "---------------------------------------------------"
	print "=========  Review Dumpster Fire Settings  ========="
	print ""

	print "About to ignite a Dumpster Fire using the following configuration:"

	PrintDumpsterFireConfig( hotDumpsterFire )

	currentDT_UTC = datetime.datetime.utcnow()

	print ""
	print "Fire will start (UTC): ", fuseDelayStr, " - Current Date/Time (UTC) =", currentDT_UTC.strftime("%x %X") 
	print ""

	choice = raw_input( "Ignite Dumpster Fire? [y/n]: ")

	if choice == "y":
		try:
			PrintBannerFlames()

			print "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "  |  +                                                         +  |"
			print "  | +++           Such dumpster fire! Much heat!              +++ |"
			print "  |  +                                                         +  |"
			print "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print ""

			IgniteDumpsterFire( hotDumpsterFire, True )

		except:
			print ""
			print "!!! Problem igniting Dumpster Fire, check your kindling."
			print ""
	else:
		print ""
		print "Dumpster fire cancelled."
		print ""
		print "Smokey the InfoSec Bear says, \"Remember, only YOU can prevent dumpster fires!\""
		print ""

	# Clear data between runs, else repeated StartDumpsterFire() calls pick up leftover crud
	del hotDumpsterFire.mFires[ : ]
	del hotDumpsterFire

	choice = raw_input( "Press return to continue... " )

	return



# ================================================================================================
#
# Function:  SelectFireCategory()
#
# Description:  Guides user through selecting Fire Categories while building a new DumpsterFire.
# Also used for browsing entire Fire Categories.
#
# ================================================================================================

def SelectFireCategory():

	print "Fire Categories:"
	print ""
	fireCatCount = 1
	for fireCategory in gFireCategories:
		print fireCatCount, "-", fireCategory
		fireCatCount = fireCatCount + 1
	print ""

	selection = -1
	while ( selection < 0 or selection > (fireCatCount - 2)):
		try:
			fireCategoryNum = raw_input( "Enter Fire Category#: " )

			selection = int ( fireCategoryNum ) - 1

			if ( fireCategory == "" or selection < 0 or selection > (fireCatCount - 1)):
				print "Invalid category selection, try again..."
				selection = -1
	
		except ValueError:
			print "Invalid category selection, try again..."
	print ""
	return selection



# ================================================================================================
#
# Function:  SelectFire()
#
# Description:  Guides user through selecting Fires while building a new DumpsterFire.
#
# ================================================================================================

def SelectFire( fireCategory ):

	# Clear values from list to avoid duplicate crud building up
	del gFires[ : ]

	# Populate the Fire modules from the supplied Fire Category
	for root, dirs, files in os.walk( "./FireModules/" + fireCategory ):
		for file in files:
			# Filter out the required __init__.py file in Fire directories
			if ( file != kLabelDirInitFile ):
				# Filter out any non-Python source files
				if file.endswith('.py'):
					gFires.append( file )

	print "Available", fireCategory, "Fires:"
	print ""
	fireCount = 1
	for fireName in gFires:
		print fireCount, "-", fireName
		fireCount = fireCount + 1
	print ""

	selection = -1

	while ( selection < 0 or selection > (fireCount - 2)):
		try:
			fireNum = raw_input( "Enter Fire #: " )

			selection = int ( fireNum ) - 1

			if ( fireNum == "" or selection < 0 or selection > (fireCount - 1)):
				print "Invalid fire selection, try again..."
				selection = -1
	
		except ValueError:
			print "Invalid fire selection, try again..."
	print ""
	return selection



# ================================================================================================
#
# Function:  PrintDateTimeStamps()
#
# Description:  Utility function for printing out the current time in UTC 
#
# ================================================================================================

def PrintDateTimeStamps():

	currentUTC = datetime.datetime.utcnow()
	print "UTC: " + currentUTC.strftime("%x %X") + "  / ",
	print time.strftime("%Z: %x %X", time.localtime(time.time()))

	return



# ================================================================================================
#
# Function:  BuildDateTime()
#
# Description:  Guides the user through building a valid Date/Time. I use separate variables for
# each element because it avoids all user-input formatting mistakes, confusion, etc.
#
# NOTE: Does not yet handle Feb. 29th on leap years. Consider it a day off. Or go to immediate
# ignition if you really want to light up that rare day.
#
# ================================================================================================

def BuildDateTime():

	year = 0
	month = 0
	day = 0
	done = 0
	fireStartTime = datetime.datetime.utcnow()

	print "Current Date/Time --",
	PrintDateTimeStamps()
	print ""
	print "MUST ENTER DATE/TIME IN UTC (see current UTC above for reference)"
	print ""

	while ( done == 0 ):
                try:
                        year = int ( raw_input( "Enter Year (YYYY): " ))

                        if ( year < 0 or year > 9999):
                                print "Invalid year, try again..."
			else:
				if ( year < fireStartTime.year ):

					choice = raw_input("You're about to hack time, are you sure? [y/n]: ")	

					if ( choice == "y" ):
						done = 1
						
				else:
					done = 1

                except ValueError:
                        print "Invalid year, try again..."

	done = 0

	while ( done == 0 ):
                try:
                        month = int ( raw_input( "Enter Month (MM): " ))

                        if ( month < 1 or month > 12 ):
                                print "Invalid month, try again..."
			else:
				if ( year == fireStartTime.year and month < fireStartTime.month ):

					choice = raw_input("You're about to hack time, are you sure? [y/n]: ")	

					if ( choice == "y" ):
						done = 1
						
				else:
					done = 1

                except ValueError:
                        print "Invalid month, try again..."

	done = 0
	doneDay = 0

	while ( done == 0 ):
                try:
			if ( month in [1,3,5,7,8,10,12] ):

				while ( doneDay == 0 ):

                        		day = int ( raw_input( "Enter Day (DD): " ))

                       			if ( day < 1 or day > 31 ):
                               			print "Invalid day, try again..."
					else:
						doneDay = 1


			elif ( month in [4,6,9,11] ):

				while ( doneDay == 0 ):

                        		day = int ( raw_input( "Enter Day (DD): " ))

                       			if ( day < 1 or day > 30 ):
                               			print "Invalid day, try again..."
					else:
						doneDay = 1


			elif ( month == 2 ):

				while ( doneDay == 0 ):

                        		day = int ( raw_input( "Enter Day (DD): " ))

                       			if ( day < 1 or day > 28 ):
                               			print "Invalid day, try again..."
					else:
						doneDay = 1

			if ( year == fireStartTime.year and month == fireStartTime.month and day < fireStartTime.day ):

				choice = raw_input("You're about to hack time, are you sure? [y/n]: ")	

				if ( choice == "y" ):
					done = 1
					
			else:
				done = 1

                except ValueError:
                        print "Invalid input, try again..."

	done = 0

	while ( done == 0 ):
                try:
                        hour = int ( raw_input( "Enter Hour (HH): " ))

                        if ( month < 0 or month > 23 ):
                                print "Invalid hour, try again..."
			else:
				if ( year == fireStartTime.year and  \
					month == fireStartTime.month and  \
					day == fireStartTime.day and  \
					hour < fireStartTime.hour ):

					choice = raw_input("You're about to hack time, are you sure? [y/n]: ")	

					if ( choice == "y" ):
						done = 1
						
				else:
					done = 1

                except ValueError:
                        print "Invalid hour, try again..."

	done = 0

	while ( done == 0 ):
                try:
                        minute = int ( raw_input( "Enter Minute (MM): " ))

                        if ( minute < 0 or minute > 59 ):
                                print "Invalid minutes, try again..."
			else:
				if ( year == fireStartTime.year and  \
					month == fireStartTime.month and  \
					day == fireStartTime.day and  \
					hour == fireStartTime.hour and  \
					minute < fireStartTime.minute ):

					choice = raw_input("You're about to hack time, are you sure? [y/n]: ")	

					if ( choice == "y" ):
						done = 1
						
				else:
					done = 1

                except ValueError:
                        print "Invalid minutes, try again..."

        return fireStartTime.replace( year=year, month=month, day=day, hour=hour, minute=minute, second=0 )



# ================================================================================================
#
# Function:  SelectDumpsterFire()
#
# Description:  Loads up the list of DumpsterFires stored in the "DumpsterFire/" directory,
# guides the user through selecting one. If no DumpsterFires are found, let them know. 
#
# ================================================================================================

def SelectDumpsterFire():

	# Clear values from list
	del gDumpsterFires[ : ]

	# Populate the DumpsterFires list with .fyr files in DumpsterFires/ directory
	for root, dirs, files in os.walk( kDumpsterFireDirectory  ):
		for file in files:
			if file.endswith('.fyr'):
				gDumpsterFires.append( file )

	selection = -1

	# If empty list, exit

	if ( len( gDumpsterFires ) == 0 ):
		print ""
		print "No DumpsterFires found in", kDumpsterFireDirectory, "directory"
		print ""
		choice = raw_input( "Press return to continue... " )

		return( selection )

	print "Available DumpsterFires:"
	print ""

	dumpsterfireCount = 1

	for dumpsterfireName in gDumpsterFires:
		print dumpsterfireCount, "-", dumpsterfireName
		dumpsterfireCount = dumpsterfireCount + 1

	print ""

	while ( selection < 0 or selection > ( dumpsterfireCount - 2 )):
		try:
			dumpsterfireNum = raw_input( "Enter DumpsterFire #: " )

			selection = int ( dumpsterfireNum ) - 1

			if ( dumpsterfireNum == "" or selection < 0 or selection > (dumpsterfireCount - 1)):
				print "Invalid DumpsterFire selection, try again..."
				selection = -1

		except ValueError:
			print "Invalid DumpsterFire selection, try again..."
	print ""
	print "Selected DumpsterFire:", gDumpsterFires[ selection ]
	print ""

	choice = raw_input( "Press return to continue... " )

	return selection



# ================================================================================================
#
# Function:  BrowseDumpsterFires()
#
# Description:  Yep, that about sums it up.
#
# ================================================================================================

def BrowseDumpsterFires():

	PrintBannerFlames()

	print "---------------------------------------------------------------------"
	print "=====================   BROWSE DUMPSTER FIRES   ====================="
	print "---------------------------------------------------------------------"
	print ""
	print "Dumpster Fires are collections of Fires (and any associated time offsets)."
	print ""
	print "Select a Dumpster Fire to view its settings."
	print ""

	selection = SelectDumpsterFire()

	if ( selection > -1 ):

		thisDumpsterFire = LoadDumpsterFireConfig( kDumpsterFireDirectory + gDumpsterFires[ selection ] )

		PrintDumpsterFireConfig( thisDumpsterFire )

		# Free up the allocated space or gets mucked up from repeated calls to this method
		del thisDumpsterFire.mFires[ : ]
		del thisDumpsterFire

		print ""
		choice = raw_input( "Press return to continue... " )

	return


# ================================================================================================
#
# Function:  DeleteDumpsterFire()
#
# Description:  Because sometimes even DumpsterFires need to be thinned out.
#
# ================================================================================================

def DeleteDumpsterFire():

	PrintBannerFlames()

	print "---------------------------------------------------------------------"
	print "=====================   DELETE DUMPSTER FIRE    ====================="
	print "---------------------------------------------------------------------"
	print ""
	print "Select a Dumpster Fire to delete."
	print ""

	selection = SelectDumpsterFire()

	if ( selection > -1 ):

		thisDumpsterFire = LoadDumpsterFireConfig( kDumpsterFireDirectory + gDumpsterFires[ selection ] )

		PrintDumpsterFireConfig( thisDumpsterFire )

		print ""
		choice = raw_input( "Delete this DumpsterFire? (y/n): " )

		if choice == "y":
			try:
				os.remove( kDumpsterFireDirectory + gDumpsterFires[ selection ] )
				print ""
				print "DumpsterFire deleted."
			except:
				print ""
				print "## Error deleting DumpsterFire"

		# Free up the allocated space or gets mucked up from repeated calls to this method
		del thisDumpsterFire.mFires[ : ]
		del thisDumpsterFire

	print ""
	choice = raw_input( "Press return to continue... " )

	return



# ================================================================================================
#
# Function:  Help()
#
# Description:  Well this went meta fast...
#
# ================================================================================================

def Help():
	print ""
	print "=====================  Using DumpsterFire  ====================="
	print ""
	print "For background and tutorial, see the presentation slides at"
	print ""
	print "https://github.com/TryCatchHCF/DumpsterFire"
	print ""
	print "The DumpsterFire toolset workflow is designed to be user-friendly and robust. Everything can be done from within the menu-driven 'dumpsterFireFactory.py' script. Launch the script and the tool will guide you as you go. You can start by browsing the existing Fire modules and saved DumpsterFires. When you're ready to create your own DumpsterFires, the tool will lead through the workflow to get the job done. Finally it will be time to ignite your DumpsterFire. After selecting the DumpsterFire of your choice, you'll review the DumpsterFire's Fire modules and settings. If everything looks good, light it up!"
	print ""
	print "When you're building a DumpsterFire, after you've chosen all of the Fire modules you wish to include, the tool will loop through the list of Fires. If a Fire has options for custom settings, the tool will call that Fire's Configure() method to present you with prompts for its settings (e.g. a target network's IP address)."
	print ""
	print "Once all of the Fires have been configured, you'll then be given the option to assign individual time delays to your Fires. This allows the DumpsterFire to better mimic real operations when executing its chain of events. For example, the first Fire may visit various hacking Websites, the next Fire then downloads a few common hacking tools before launching the third Fire which starts scanning the local network. If this all happened within seconds of each other, no SOC analyst is going to believe it was a human. By adding several minutes or even hours between those events, you create a more realistic chain of events."
	print ""
	print "After all of the Fires have been configured and optional individual Fire delays assigned, you'll be asked to name your DumpsterFire. Do not use spaces or odd special characterse, just stick to letter, numbers, underscores, and hyphens."
	print ""
	print "Voila! You have now created your first DumpsterFire. Time to choose ignite one."
	print ""
	print "When you're ready to ignite a DumpsterFire, the tool will first show you the DumpsterFire's settings. If everything looks good, you'll be asked if you want to assign a date-time delay before igniting. All date-time processing is done in UTC to ensure consistent execution regardless of your DumpsterFire's location of execution. Otherwise you can decline the date-time delay and execution will begin immediately after you give final confirmation."
	print ""
	print "As the DumpsterFire executes, you'll be given regular date-time stamped feedback on each Fire's status and critical events. This not only helps you track progress, but also provides a chronological record of your DumpsterFire's activities - critical in coordinating and deconflicting your events from the general background noise that floods every SOC. You can also hand over the chronological record to your external clients after your operations are complete, as a value-added record of your activites that they can use to review their sensor and alert settings. All with no extra effort on your part."
	print ""
	choice = raw_input( "Press return to continue... " )



# ================================================================================================
#
# Function:  IgniteFire()
#
# Description:  Loads the Fire class from its package, sets its parameters, lights it up!
#
# ================================================================================================

def IgniteFire( modulePath, fireName, params ):

	try:
		# Load Fire module (Python class)
		currentFireClass = getattr( importlib.import_module( modulePath, fireName ), fireName )

		# Create instance of Fire, with parameters that were stored in parent DumpsterFire
		thisFire = currentFireClass( "" )

	except:
		print "### IgniteFire: Error loading fire."
		print "Module Path:", modulePath
		print "Fire Name:", fireName

	try:
		thisFire.SetParameters( params )
		thisFire.Ignite() 

	except:
		print "### IgniteFire: Error while running Fire()"

	return



# ================================================================================================
#
# Function:  MainMenu()
#
# Description:  No one will ever guess what this function does. Let's keep it our little secret.
#
# ================================================================================================

def MainMenu():

	selectionErrorMsg = "1-9 are your options. Try again."
	notDone = 1

	while ( notDone ): 

		PrintBannerFlames()

		print "    ____   /((_)   )\  ' /(/(   )\  _            _____        /((_)  "
 		print "   |  _ \ _   _ _ __ ___  _ __  ___| |_ ___ _ __|  ___( )_ __ ___    "
 		print "   | | | | | | | '_ V _ \| '_ \/ __| __/ _ \ '__| |_  | | '__/ _ \   "
 		print "   | |_| | |_| | | | | | | |_) \__ \ ||  __/ |  |  _| | | | |  __/   "
 		print "   |____/ \__,_|_| |_| |_| .__/|___/\__\___|_|  |_|   |_|_|  \___|   "
		print "                         |_|                                         "
		print ""
		print "                  \"Security Incidents In A Box\""
		print ""
		print "   Generate Time-Delayed, Distributed Incidents for Red/Blue Teams   "
		print ""
		print "                      Written by TryCatchHCF"
		print "                  https://github.com/TryCatchHCF"
		print ""

		print ""
		print "--------------------------------------------------"
		print "===========  DumpsterFire Main Menu  ============="
		print "--------------------------------------------------"
		print ""
		print "1) Build New Dumpster Fire"
		print "2) Configure Existing Dumpster Fire"
		print "3) Ignite a Dumpster Fire"
		print "4) Browse Dumpster Fires"
		print "5) Browse Fires"
		print "6) Delete Dumpster Fire"
		print "7) Help / Basic Usage"
		print "8) Exit"
		print ""
	
		invalidSelection = 1
	
		while ( invalidSelection ):
			try:
				choice = int( raw_input( "Selection: " ))
	
				if ( choice > 0 and choice < 9 ):
					invalidSelection = 0
				else:
					print selectionErrorMsg
	
			except ValueError:
				print selectionErrorMsg
	
		if choice == 1:
			BuildDumpsterFire()	
		elif choice == 2:
			ConfigureExistingDumpsterFire()
		elif choice == 3:
			StartDumpsterFire()
		elif choice == 4:
			BrowseDumpsterFires()
		elif choice == 5:
			BrowseFires()
		elif choice == 6:
			DeleteDumpsterFire()
		elif choice == 7:
			Help()
		elif choice == 8:
			notDone = 0
		else:
			print selectionErrorMsg
	
	byeArray = ("Bye!", "Ciao!", "Adios!", "Aloha!", "Hei hei!", "Bless bless!", "Hej da!", "Tschuss!", "Adieu!", "Cheers!")

	print ""
	print random.choice( byeArray )
	print ""

## ==============================  Main Loop  ================================

def main():

	MainMenu()
	return

if __name__ == "__main__":
	main()

