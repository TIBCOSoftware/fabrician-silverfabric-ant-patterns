import os
import os.path
import sys
import traceback

def mkdir_p(path, mode=0700):
	if not os.path.isdir(path):
 		logger.info("Creating directory:" + path)
 		os.makedirs(path, mode)
        
def prepareWorkDirectory():
	logger.info("Enter prepareWorkDirectory")
	
	try:
		logger.info("Enter prepareWorkDirectory")
		
		dataStoreLocation = runtimeContext.getVariable("DATASTORE_LOCATION").value
		mkdir_p(dataStoreLocation)
	except BaseException, value:
		logger.severe("Unexpected exception in prepareWorkDirectory:" + `value`)
		traceback.print_exc()
	finally:
		proxy.prepareWorkDirectory()
        
	logger.info("Exit prepareWorkDirectory")
	