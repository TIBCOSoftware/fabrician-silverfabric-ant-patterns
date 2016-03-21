@echo off

call "%WL_HOME%/server/bin/setWLSEnv.cmd"

set CLASSPATH="%CLASSPATH%;%WL_HOME%/server/lib;%WL_HOME%/common/lib"

"%JAVA_HOME%/bin/java" weblogic.WLST "%DS_WEBLOGIC_BASE%/wlst/configDomain.py"
