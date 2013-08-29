#	"$Name:  $";
#	"$Header:  $";
#=============================================================================
#
# file :        XMLConfigServer.py
#
# description : Python source for the XMLConfigServer and its commands. 
#                The class is derived from Device. It represents the
#                CORBA servant object which will be accessed from the
#                network. All commands which can be executed on the
#                XMLConfigServer are implemented in this file.
#
# project :     TANGO Device Server
#
# $Author:  $
#
# $Revision:  $
#
# $Log:  $
#
# copyleft :    European Synchrotron Radiation Facility
#               BP 220, Grenoble 38043
#               FRANCE
#
#=============================================================================
#  		This file is generated by POGO
#	(Program Obviously used to Generate tango Object)
#
#         (c) - Software Engineering Group - ESRF
#=============================================================================
#


import PyTango
import sys

import ndtsconfigserver
from ndtsconfigserver.XMLConfigurator import XMLConfigurator as XMLC


#==================================================================
#   XMLConfigServer Class Description:
#
#         Configuration Server based on MySQL database
#
#==================================================================
# 	Device States Description:
#
#   DevState.OPEN :     Open connection to the database
#   DevState.ON :       Server is ON
#   DevState.RUNNING :  Performing a query
#==================================================================


class XMLConfigServer(PyTango.Device_4Impl):

#--------- Add you global variables here --------------------------

#------------------------------------------------------------------
#	Device constructor
#------------------------------------------------------------------
	def __init__(self,cl, name):
		self.xmlc = None
		PyTango.Device_4Impl.__init__(self,cl,name)
		XMLConfigServer.init_device(self)

#------------------------------------------------------------------
#	Device destructor
#------------------------------------------------------------------
	def delete_device(self):
		print "[Device delete_device method] for device",self.get_name()
		if hasattr(self,"xmlc") and self.xmlc:
			if hasattr(self.xmlc, "close"):
				self.xmlc.close()
			del self.xmlc
			self.xmlc =None
		self.set_state(PyTango.DevState.OFF)


#------------------------------------------------------------------
#	Device initialization
#------------------------------------------------------------------
	def init_device(self):
		print "In ", self.get_name(), "::init_device()"
		self.xmlc = XMLC()
		self.set_state(PyTango.DevState.ON)
		self.get_device_properties(self.get_device_class())
		self.xmlc.versionLabel = self.VersionLabel

#------------------------------------------------------------------
#	Always excuted hook method
#------------------------------------------------------------------
	def always_executed_hook(self):
		print "In ", self.get_name(), "::always_excuted_hook()"

#==================================================================
#
#	XMLConfigServer read/write attribute methods
#
#==================================================================
#------------------------------------------------------------------
#	Read Attribute Hardware
#------------------------------------------------------------------
	def read_attr_hardware(self,data):
		print "In ", self.get_name(), "::read_attr_hardware()"



#------------------------------------------------------------------
#	Read XMLString attribute
#------------------------------------------------------------------
	def read_XMLString(self, attr):
		print "In ", self.get_name(), "::read_XMLString()"
		
		#	Add your own code here
		
#		attr_XMLString_read = "Hello Tango world"
		attr.set_value(self.xmlc.xmlConfig)


#------------------------------------------------------------------
#	Write XMLString attribute
#------------------------------------------------------------------
	def write_XMLString(self, attr):
		print "In ", self.get_name(), "::write_XMLString()"
		
		self.xmlc.xmlConfig = attr.get_write_value()
		print "Attribute value = ", self.xmlc.xmlConfig

		#	Add your own code here


#---- XMLString attribute State Machine -----------------
	def is_XMLString_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read JSONSettings attribute
#------------------------------------------------------------------
	def read_JSONSettings(self, attr):
		print "In ", self.get_name(), "::read_JSONSettings()"
		
		#	Add your own code here
		
		attr.set_value(self.xmlc.jsonSettings)


#------------------------------------------------------------------
#	Write JSONSettings attribute
#------------------------------------------------------------------
	def write_JSONSettings(self, attr):
		print "In ", self.get_name(), "::write_JSONSettings()"
		self.xmlc.jsonSettings = attr.get_write_value()
		print "Attribute value = ", self.xmlc.jsonSettings

		#	Add your own code here


#---- JSONSettings attribute State Machine -----------------
	def is_JSONSettings_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.OPEN,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Read Version attribute
#------------------------------------------------------------------
	def read_Version(self, attr):
		print "In ", self.get_name(), "::read_Version()"
		
		#	Add your own code here
		self.get_device_properties(self.get_device_class())
		self.xmlc.versionLabel = self.VersionLabel
		attr.set_value(self.xmlc.version)


#---- Version attribute State Machine -----------------
	def is_Version_allowed(self, req_type):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True



#==================================================================
#
#	XMLConfigServer command methods
#
#==================================================================

#------------------------------------------------------------------
#	Open command:
#
#	Description: Opens connection to the database
#                
#------------------------------------------------------------------
	def Open(self):
		print "In ", self.get_name(), "::Open()"
		#	Add your own code here
		try:
			if self.get_state() == PyTango.DevState.OPEN:
				self.set_state(PyTango.DevState.RUNNING)
				self.xmlc.close()
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.open()
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.ON)


#---- Open command State Machine -----------------
	def is_Open_allowed(self):
		if self.get_state() in [PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Close command:
#
#	Description: Closes connection into the database
#                
#------------------------------------------------------------------
	def Close(self):
		print "In ", self.get_name(), "::Close()"
		#	Add your own code here

		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.close()
			self.set_state(PyTango.DevState.ON)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.ON)


#---- Close command State Machine -----------------
	def is_Close_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	Components command:
#
#	Description: Returns a list of required components
#                
#	argin:  DevVarStringArray	list of component names
#	argout: DevVarStringArray	list of required components
#------------------------------------------------------------------
	def Components(self, argin):
		print "In ", self.get_name(), "::Components()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			argout = self.xmlc.components(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)
		
		return argout


#---- Components command State Machine -----------------
	def is_Components_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	DataSources command:
#
#	Description: Return a list of required DataSources
#                
#	argin:  DevVarStringArray	list of DataSource names
#	argout: DevVarStringArray	list of required DataSources
#------------------------------------------------------------------
	def DataSources(self, argin):
		print "In ", self.get_name(), "::DataSources()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			argout = self.xmlc.dataSources(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)
		
		return argout


#---- DataSources command State Machine -----------------
	def is_DataSources_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	AvailableComponents command:
#
#	Description: Returns a list of available component names
#                
#	argout: DevVarStringArray	list of available component names
#------------------------------------------------------------------
	def AvailableComponents(self):
		print "In ", self.get_name(), "::AvailableComponents()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			argout = self.xmlc.availableComponents()
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)
		
		return argout


#---- AvailableComponents command State Machine -----------------
	def is_AvailableComponents_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	AvailableDataSources command:
#
#	Description: Returns a list of available DataSource names
#                
#	argout: DevVarStringArray	list of available DataSource names
#------------------------------------------------------------------
	def AvailableDataSources(self):
		print "In ", self.get_name(), "::AvailableDataSources()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			argout = self.xmlc.availableDataSources()
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)
		
		return argout


#---- AvailableDataSources command State Machine -----------------
	def is_AvailableDataSources_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	StoreComponent command:
#
#	Description: Stores the component from XMLString
#                
#	argin:  DevString	component name
#------------------------------------------------------------------
	def StoreComponent(self, argin):
		print "In ", self.get_name(), "::StoreComponent()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.storeComponent(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)


#---- StoreComponent command State Machine -----------------
	def is_StoreComponent_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	StoreDataSource command:
#
#	Description: Stores the DataSource from XMLString
#                
#	argin:  DevString	datasource name
#------------------------------------------------------------------
	def StoreDataSource(self, argin):
		print "In ", self.get_name(), "::StoreDataSource()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.storeDataSource(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)


#---- StoreDataSource command State Machine -----------------
	def is_StoreDataSource_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	CreateConfiguration command:
#
#	Description: Creates the NDTS configuration script from the given components. The result is strored in XMLString
#                
#	argin:  DevVarStringArray	list of component names
#------------------------------------------------------------------
	def CreateConfiguration(self, argin):
		print "In ", self.get_name(), "::CreateConfiguration()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.createConfiguration(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)


#---- CreateConfiguration command State Machine -----------------
	def is_CreateConfiguration_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	DeleteComponent command:
#
#	Description: Deletes the given component
#                
#	argin:  DevString	component name
#------------------------------------------------------------------
	def DeleteComponent(self, argin):
		print "In ", self.get_name(), "::DeleteComponent()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.deleteComponent(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)


#---- DeleteComponent command State Machine -----------------
	def is_DeleteComponent_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	DeleteDataSource command:
#
#	Description: Deletes the given datasource
#                
#	argin:  DevString	datasource name
#------------------------------------------------------------------
	def DeleteDataSource(self, argin):
		print "In ", self.get_name(), "::DeleteDataSource()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.deleteDataSource(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)


#---- DeleteDataSource command State Machine -----------------
	def is_DeleteDataSource_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	SetMandatoryComponents command:
#
#	Description: Sets the mandatory components
#                
#	argin:  DevVarStringArray	component names
#------------------------------------------------------------------
	def SetMandatoryComponents(self, argin):
		print "In ", self.get_name(), "::SetMandatoryComponents()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.setMandatoryComponents(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)


#---- SetMandatoryComponents command State Machine -----------------
	def is_SetMandatoryComponents_allowed(self):
		if self.get_state() in [PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	MandatoryComponents command:
#
#	Description: Sets the mandatory components
#                
#	argout: DevVarStringArray	component names
#------------------------------------------------------------------
	def MandatoryComponents(self):
		print "In ", self.get_name(), "::MandatoryComponents()"
		#	Add your own code here
		
		try:
			self.set_state(PyTango.DevState.RUNNING)
			argout = self.xmlc.mandatoryComponents()
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)
		return argout


#---- MandatoryComponents command State Machine -----------------
	def is_MandatoryComponents_allowed(self):
		if self.get_state() in [PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	UnsetMandatoryComponents command:
#
#	Description: It removes the given components from the mandatory components
#                
#	argin:  DevVarStringArray	list of component names
#------------------------------------------------------------------
	def UnsetMandatoryComponents(self, argin):
		print "In ", self.get_name(), "::UnsetMandatoryComponents()"
		#	Add your own code here
		try:
			self.set_state(PyTango.DevState.RUNNING)
			self.xmlc.unsetMandatoryComponents(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)


#---- UnsetMandatoryComponents command State Machine -----------------
	def is_UnsetMandatoryComponents_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#------------------------------------------------------------------
#	ComponentDataSources command:
#
#	Description: returns a list of datasource names for a given component
#                
#	argin:  DevString	component name
#	argout: DevVarStringArray	list of datasource names
#------------------------------------------------------------------
	def ComponentDataSources(self, argin):
		print "In ", self.get_name(), "::ComponentDataSources()"
		#	Add your own code here
		try:
			print "component name",argin
			self.set_state(PyTango.DevState.RUNNING)
			argout = self.xmlc.componentDataSources(argin)
			self.set_state(PyTango.DevState.OPEN)
 		finally:
			if self.get_state() == PyTango.DevState.RUNNING:
				self.set_state(PyTango.DevState.OPEN)
		
		return argout


#---- ComponentDataSources command State Machine -----------------
	def is_ComponentDataSources_allowed(self):
		if self.get_state() in [PyTango.DevState.ON,
		                        PyTango.DevState.RUNNING]:
			#	End of Generated Code
			#	Re-Start of Generated Code
			return False
		return True


#==================================================================
#
#	XMLConfigServerClass class definition
#
#==================================================================
class XMLConfigServerClass(PyTango.DeviceClass):

	#	Class Properties
	class_property_list = {
		}


	#	Device Properties
	device_property_list = {
		'VersionLabel':
			[PyTango.DevString,
			"version label",
			[ "XCS" ] ],
		}


	#	Command definitions
	cmd_list = {
		'Open':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'Close':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVoid, ""]],
		'Components':
			[[PyTango.DevVarStringArray, "list of component names"],
			[PyTango.DevVarStringArray, "list of required components"]],
		'DataSources':
			[[PyTango.DevVarStringArray, "list of DataSource names"],
			[PyTango.DevVarStringArray, "list of required DataSources"]],
		'AvailableComponents':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVarStringArray, "list of available component names"]],
		'AvailableDataSources':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVarStringArray, "list of available DataSource names"]],
		'StoreComponent':
			[[PyTango.DevString, "component name"],
			[PyTango.DevVoid, ""]],
		'StoreDataSource':
			[[PyTango.DevString, "datasource name"],
			[PyTango.DevVoid, ""]],
		'CreateConfiguration':
			[[PyTango.DevVarStringArray, "list of component names"],
			[PyTango.DevVoid, ""]],
		'DeleteComponent':
			[[PyTango.DevString, "component name"],
			[PyTango.DevVoid, ""]],
		'DeleteDataSource':
			[[PyTango.DevString, "datasource name"],
			[PyTango.DevVoid, ""]],
		'SetMandatoryComponents':
			[[PyTango.DevVarStringArray, "component names"],
			[PyTango.DevVoid, ""]],
		'MandatoryComponents':
			[[PyTango.DevVoid, ""],
			[PyTango.DevVarStringArray, "component names"]],
		'UnsetMandatoryComponents':
			[[PyTango.DevVarStringArray, "list of component names"],
			[PyTango.DevVoid, ""]],
		'ComponentDataSources':
			[[PyTango.DevString, "component name"],
			[PyTango.DevVarStringArray, "list of datasource names"]],
		}


	#	Attribute definitions
	attr_list = {
		'XMLString':
			[[PyTango.DevString,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'label':"XML configuration",
				'description':"It allows to pass XML strings into database during performing StoreComponent and StoreDataSource.\nMoreover, after performing CreateConfiguration it contains the resulting XML configuration.",
			} ],
		'JSONSettings':
			[[PyTango.DevString,
			PyTango.SCALAR,
			PyTango.READ_WRITE],
			{
				'label':"Arguments of MySQLdb.connect(...)",
				'description':"The JSON string with parameters of MySQLdb.connect(...).",
				'Memorized':"true",
			} ],
		'Version':
			[[PyTango.DevString,
			PyTango.SCALAR,
			PyTango.READ],
			{
				'label':"configuration version",
				'description':"configuration version",
			} ],
		}


#------------------------------------------------------------------
#	XMLConfigServerClass Constructor
#------------------------------------------------------------------
	def __init__(self, name):
		PyTango.DeviceClass.__init__(self, name)
		self.set_type(name);
		print "In XMLConfigServerClass  constructor"

#==================================================================
#
#	XMLConfigServer class main method
#
#==================================================================
if __name__ == '__main__':
	try:
		py = PyTango.Util(sys.argv)
		py.add_TgClass(XMLConfigServerClass,XMLConfigServer,'XMLConfigServer')

		U = PyTango.Util.instance()
		U.server_init()
		U.server_run()

	except PyTango.DevFailed,e:
		print '-------> Received a DevFailed exception:',e
	except Exception,e:
		print '-------> An unforeseen exception occured....',e
