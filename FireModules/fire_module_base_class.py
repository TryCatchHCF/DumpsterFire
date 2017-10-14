#!/usr/bin/python
#
# Filename:  fire_module_base_class.py
#
# Version: 1.0.0
#
# Author:  Joe Gervais (TryCatchHCF)
#
# Summary:
#
#	Base class from which Fire modules inherit. Shouldn't ever be instantiated
#	as an object, is instead a definition of the Fire modules' interfaces.
#

class FireModule:

	def Configure():
		print "Base Class: Getting configs!"
		return

	def GetParameters():
		return "Base Class: Parameters!"

	def SetParameters( parametersStr ):
		print "Base Class: Setting parameters!"
		print parametersStr
		return

	def ActivateLogging( logFlag ):
		print "Base Class: Setting Logging flag!"
		print logFlag
		return

	def Ignite():
		print "Base Class: Such Fire! Much Heat!"
		return

