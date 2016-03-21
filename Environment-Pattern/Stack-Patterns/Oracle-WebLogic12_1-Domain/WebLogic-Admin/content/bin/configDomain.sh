#!/bin/sh

. $WL_HOME/server/bin/setWLSEnv.sh

CLASSPATH=$CLASSPATH:$WL_HOME/server/lib:$WL_HOME/common/lib
export CLASSPATH

chmod u+x $JAVA_HOME/bin/java

$JAVA_HOME/bin/java weblogic.WLST $DS_WEBLOGIC_BASE/wlst/configDomain.py
