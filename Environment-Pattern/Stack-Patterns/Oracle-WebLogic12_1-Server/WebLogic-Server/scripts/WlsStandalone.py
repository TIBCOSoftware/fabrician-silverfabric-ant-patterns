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
        domainDir = getVariableValue("WL_DOMAIN_DIR", "")
        wlHome = getVariableValue("WL_HOME", "")
        baseDir = getVariableValue("DS_WEBLOGIC_BASE", "")
         
        src = os.path.join(baseDir, "wl_home")
        if os.path.isdir(src):
            logger.info("Copy " + src + " to " + wlHome)
            distutils.dir_util.copy_tree(src, wlHome, 0, 0)
                
        src = os.path.join(baseDir, "domain_home")
        if os.path.isdir(src):
            logger.info("Copy " + src + " to " + domainDir)
            distutils.dir_util.copy_tree(src, domainDir, 0, 0)
    except:
        type, value, traceback = sys.exc_info()
        logger.finer("WebLogicServer initialization  error:" + `value`)
        raise
    finally:
        proxy.doInit(additionalVariables)
        
    logger.info("Exit WebLogicServer:doInit")

