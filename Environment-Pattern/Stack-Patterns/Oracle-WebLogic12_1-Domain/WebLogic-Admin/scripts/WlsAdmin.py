import os
import os.path
import sys
import traceback
import time
import distutils.dir_util
from subprocess import call
from distutils import dir_util
import stat
from datetime import datetime

from com.datasynapse.fabric.util import ContainerUtils
from com.datasynapse.fabric.common import RuntimeContextVariable

class WebLogicServer:
	def __init__(self, additionalVariables):
		" This class represents a WebLogic Server"
		try:
			self.__initServerInfo(additionalVariables)
			
			src = os.path.join(self.__baseDir, "WL_HOME")
			if os.path.isdir(src):
				logger.info("Copy " + src + " to " + self.__wlHome)
				distutils.dir_util.copy_tree(src, self.__wlHome, 0, 0)
				
			src = os.path.join(self.__baseDir, "DOMAIN_HOME")
			if os.path.isdir(src):
				logger.info("Copy " + src + " to " + self.__domainDir)
				distutils.dir_util.copy_tree(src, self.__domainDir, 0, 0)
				
		except:
			type, value, traceback = sys.exc_info()
			logger.finer("WebLogicServer initialization  error:" + `value`)
			raise
				
	def __initServerInfo(self, additionalVariables):
		"initialize server info"
		self.__domainDir = getVariableValue("WL_DOMAIN_DIR", "")
		self.__wlsUser = getVariableValue("WLS_USER")
		self.__wlsPwd = getVariableValue("WLS_PW")
		
		self.__wlHome = getVariableValue("WL_HOME", "")
  		
  		self.__baseDir = getVariableValue("DS_WEBLOGIC_BASE", "")
  		self.__workDir = getVariableValue("ENGINE_WORK_DIR", "")
         
		serverAddrs = getVariableValue("LISTEN_ADDRESS")
		httpPortStr = getVariableValue("HTTP_PORT", "")
		self.__wlsUrl = "t3://" + serverAddrs +":"+  httpPortStr
		additionalVariables.add(RuntimeContextVariable("WLS_URL", self.__wlsUrl, RuntimeContextVariable.STRING_TYPE))
		changePermissions(self.__baseDir)
		
	def __configureDomain(self):
		"configure domain"
		configureDomainCommand = "configDomain.sh"
		if ContainerUtils.isWindows():
			configureDomainCommand = "configDomain.bat"
		cmdfile = os.path.join(self.__baseDir, "bin", configureDomainCommand)
		logger.info("Configure domain")
		self.__copyContainerEnvironment()
		retcode = call([cmdfile])
		logger.info("Return code: " + str(retcode))
		
	def __copyContainerEnvironment(self):
		" copy container environment"
    
        # we need to unset LD_PRELOAD or we can get errors
		os.environ["LD_PRELOAD"] = ""
    
		count = runtimeContext.variableCount
		for i in range(0, count, 1):
			rtv = runtimeContext.getVariable(i)
			if rtv.type == "Environment":
				os.environ[rtv.name] = rtv.value
			
	def install(self, info):
		"install"
		self.__configureDomain()
			
def changePermissions(dir):
	logger.info("chmod:"+dir)
	os.chmod(dir, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP  | stat.S_IXGRP | stat.S_IROTH  | stat.S_IXOTH)
      
	for dirpath, dirnames, filenames in os.walk(dir):
		for dirname in dirnames:
			dpath = os.path.join(dirpath, dirname)
			os.chmod(dpath, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP  | stat.S_IXGRP | stat.S_IROTH  | stat.S_IXOTH)
	   	
	   	for filename in filenames:
	   		filePath = os.path.join(dirpath, filename)
	   		os.chmod(filePath, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP  | stat.S_IXGRP | stat.S_IROTH  | stat.S_IXOTH)
	   
def getVariableValue(name, value=None):
    "get runtime variable value"
    var = runtimeContext.getVariable(name)
    if var != None:
        value = var.value
    
    return value

def doInit(additionalVariables):
	"do init"
	logger.info("Enter WebLogicServer:doInit")
	
	try:
		weblogicServer = WebLogicServer(additionalVariables)
		weblogicServerRcv = RuntimeContextVariable("WEBLOGIC_SERVER_OBJECT", weblogicServer, RuntimeContextVariable.OBJECT_TYPE)
		runtimeContext.addVariable(weblogicServerRcv)
	except:
		type, value, traceback = sys.exc_info()
		logger.severe("Unexpected exception in WebLogicServer:doInit:" + `value`)
		raise
	finally:
		proxy.doInit(additionalVariables)
		
	logger.info("Exit WebLogicServer:doInit")

def doInstall(info):
	" do install of activation info"
	
	logger.info("WebLogicServer: doInstall:Enter")
	try:
		weblogicServer = getVariableValue("WEBLOGIC_SERVER_OBJECT")
		if weblogicServer:
			weblogicServer.install(info)
		proxy.doInstall(info)
	except:
		type, value, traceback = sys.exc_info()
		logger.severe("Unexpected error in WebLogicServer:doInstall:" + `value`)
	finally:
		proxy.doInstall(info)
        
	logger.info("WebLogicServer: doInstall:Exit")
