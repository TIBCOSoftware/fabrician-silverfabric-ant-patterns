# Create Oracle JDBC resource
import sys, traceback
import os
import os.path
from java.util import Properties
from java.io import FileReader


def getPropertyPathList(folder):
	pathList = []
	
	try:
		dir = os.path.join("${DS_WEBLOGIC_BASE}", "config", folder)
		if os.path.isdir(dir):
			list = os.listdir(dir)
			for entry in list:
				path = os.path.join(dir, entry)
				if os.path.isfile(path):
					pathList.append(path)
	except:
		type, value, traceback = sys.exc_info()
		print "Error get property file list:" + folder + ":"+ `value`
				
	return pathList
		
def loadProps(path):
	props = Properties()
	try:
		propReader = FileReader(path)
		props.load(propReader)
		propReader.close()
	except:
		type, value, traceback = sys.exc_info()
		print "Error loading properties from file:" + path +":" + `value`
	
	return props

def addTargets(mbean, targets):
	if targets:
		targetList = targets.split(",")
		for target in targetList:
			mbeanTarget = getMBean(target.strip())
			mbean.addTarget(mbeanTarget)
		

def configureClusters():
	pathList = getPropertyPathList("clusters")
	for path in pathList:
		props = loadProps(path)
			
		clusterName = props.getProperty("Cluster")
		print "Create cluster " + clusterName
		cluster = create(clusterName, "Cluster")
		
		clusterMessagingMode=props.getProperty("ClusterMessagingMode")
		cluster.setClusterMessagingMode(clusterMessagingMode)
		
		if clusterMessagingMode == "multicast":
			address= props.getProperty("MulticastAddress")
			print "Set multicast address:" + address
			cluster.setMulticastAddress(address)
		
			port = props.getProperty("MulticastPort")
			print "Set multicast port:" + port
			cluster.setMulticastPort(int(port))
		
			ttl=props.getProperty("MulticastTTL")
			print "Set multi cast TTL:" + ttl
			cluster.setMulticastTTL(int(ttl))
		
		servers = props.getProperty("Servers")
		if servers:
			serversList = servers.split(",")
			for serverName in serversList:
				server = create(serverName, "Server")
				server.setCluster(cluster)
			
def configureFileStores():
	pathList = getPropertyPathList("file-stores")
	for path in pathList:
		props = loadProps(path)
			
		fileStoreName = props.getProperty("Name")
		print "create FileStore " + fileStoreName
		fileStore =  create(fileStoreName,'FileStore')
		fileStore.setDirectory(props.getProperty("Directory"))
		targets = props.getProperty("Targets")
		addTargets(fileStore, targets)
		

def configureJdbcStores():
	print "Configure JDBC Stores"
	pathList = getPropertyPathList("jdbc-stores")
	for path in pathList:
		props = loadProps(path)
			
		jdbcStoreName = props.getProperty("Name")
		print "create JDBCStore " + jdbcStoreName
		jdbcStore =  create(jdbcStoreName,'JDBCStore')
		datasource = props.getProperty("DataSource")
		jdbcStore.setDataSource(getMBean("/JDBCSystemResources/" + datasource))
		prefixName = props.getProperty("PrefixName")
		if prefixName:
			jdbcStore.setPrefixName(prefixName)
		logicalName = props.getProperty("LogicalName")
		if logicalName:
			jdbcStore.setLogicalName(logicalName)
		targets = props.getProperty("Targets")
		addTargets(jdbcStore, targets)
		
def configureDistributedQueues():
	print "Configure DistributedQueues"
	pathList = getPropertyPathList("jms-distributed-queues")
	for path in pathList:
		props = loadProps(path)
		
		jmsSystemResourceName = "/JMSSystemResources/"+props.getProperty("JMSSystemResource")
		jmsSystemResource=getMBean(jmsSystemResourceName)
		theJMSResource = jmsSystemResource.getJMSResource()

		distQueueName = props.getProperty("Name")
		print "create DistributedQueue " + distQueueName
		distQueue = theJMSResource.createDistributedQueue(distQueueName)
		distQueue.setJNDIName(props.getProperty("JNDIName"))
		
		loadBlancingPolicy = props.getProperty("LoadBalancingPolicy")
		if loadBlancingPolicy:
			distQueue.setLoadBalancingPolicy(loadBlancingPolicy)
		forwadDelay = props.getProperty("ForwardDelay")
		if forwadDelay:
			distQueue.setForwardDelay(int(forwadDelay))
		targets = props.getProperty("Targets")
		addTargets(distQueue, targets)
		
def configureDistributedTopics():
	print "Configure DistributedTopics"
	pathList = getPropertyPathList("jms-distributed-topics")
	for path in pathList:
		props = loadProps(path)
		
		jmsSystemResource=getMBean("/JMSSystemResources/"+props.getProperty("JMSSystemResource"))
		theJMSResource = jmsSystemResource.getJMSResource()
		
		distTopicName = props.getProperty("Name")
		print "create DistributedTopic " + distTopicName
		distTopic = theJMSResource.createDistributedTopic(distTopicName)
		distTopic.setJNDIName(props.getProperty("JNDIName"))
		loadBlancingPolicy = props.getProperty("LoadBalancingPolicy")
		if loadBlancingPolicy:
			distTopic.setLoadBalancingPolicy(loadBlancingPolicy)
		targets = props.getProperty("Targets")
		addTargets(distTopic, targets)
		

def configureQueues():
	print "Configure Queues"
	pathList = getPropertyPathList("jms-queues")
	for path in pathList:
		props = loadProps(path)
		
		jmsSystemResource=getMBean("/JMSSystemResources/"+props.getProperty("JMSSystemResource"))
		theJMSResource = jmsSystemResource.getJMSResource()
		
		queueName = props.getProperty("Name")
		print "create Queue " + queueName
		queue = theJMSResource.createQueue(queueName)
		queue.setJNDIName(props.getProperty("JNDIName"))
		subdpeloymentName = props.getProperty("SubDeploymentName")
		if subdpeloymentName:
			queue.setSubDeploymentName(subdpeloymentName)
		targets = props.getProperty("Target")
		addTargets(queue, targets)
		
def configureTopics():
	print "Configure Topics"
	pathList = getPropertyPathList("jms-topics")
	for path in pathList:
		props = loadProps(path)
		
		jmsSystemResource=getMBean("/JMSSystemResources/"+props.getProperty("JMSSystemResource"))
		theJMSResource = jmsSystemResource.getJMSResource()
		
		topicName = props.getProperty("Name")
		print "create Topic " + topicName
		topic = theJMSResource.createTopic(topicName)
		topic.setJNDIName(props.getProperty("JNDIName"))
		subdpeloymentName = props.getProperty("SubDeploymentName")
		if subdpeloymentName:
			topic.setSubDeploymentName(subdpeloymentName)
		targets = props.getProperty("Target")
		addTargets(topic, targets)

def configureJmsSubDeployments():
	print "Configure SubDeployments"
	pathList = getPropertyPathList("jms-sub-deployments")
	for path in pathList:
		props = loadProps(path)
		
		jmsSystemResource=getMBean("/JMSSystemResources/"+props.getProperty("JMSSystemResource"))
		
		subDeploymentName = props.getProperty("Name")
		print "create JMS SubDeployment " + subDeploymentName
		subDeployment = jmsSystemResource.createSubDeployment(subDeploymentName)
		targets = props.getProperty("Targets")
		addTargets(subDeployment, targets)
		
		
def configureJmsServers():
	print "Configure JMS Servers"
	pathList = getPropertyPathList("jms-servers")
	for path in pathList:
		props = loadProps(path)
			
		jmsServerName = props.getProperty("Name")
		print "create JMSServer " + jmsServerName
		jmsServer =  create(jmsServerName,'JMSServer')
		store = props.getProperty("Store")
		if store:
			jmsServer.setPersistentStore(getMBean(store))
		targets = props.getProperty("Target")
		addTargets(jmsServer, targets)

def configureJmsConnectionFactories():
	print "Configure JMS Connection Factories"
	pathList = getPropertyPathList("jms-connection-factories")
	for path in pathList:
		props = loadProps(path)
	
		jmsSystemResource=getMBean("/JMSSystemResources/"+props.getProperty("JMSSystemResource"))
		theJMSResource = jmsSystemResource.getJMSResource()
		jmsConFactoryName = props.getProperty("Name")
		print "create JMS Factory " + jmsConFactoryName
		jmsConFactory = theJMSResource.createConnectionFactory(jmsConFactoryName)
		
		jmsConFactory.setJNDIName(props.getProperty("JNDIName"))
		subDepName = props.getProperty("SubDeploymentName")
		if subDepName:
			jmsConFactory.setSubDeploymentName(subDepName)
		targets = props.getProperty("Targets")
		addTargets(jmsConFactory, targets)
			
def configureJmsSystemResources():
	print "Configure JMS System Resources"
	pathList = getPropertyPathList("jms-system-resources")
	for path in pathList:
		props = loadProps(path)
			
		jmsSysResName = props.getProperty("Name")
		print "create JMSSystemResource " + jmsSysResName
		jmsSysRes = create(jmsSysResName,"JMSSystemResource")
		targets = props.getProperty("Targets")
		addTargets(jmsSysRes, targets)
			
def configureJdbcSystemResources():
	print "Configure JDBC System Resources"
	pathList = getPropertyPathList("jdbc-system-resources")
	for path in pathList:
		props = loadProps(path)
	
		dsName = props.getProperty("Name")
		print "create JDBCSystemResource " + dsName
		jdbcSR = create(dsName,'JDBCSystemResource')
		theJDBCResource = jdbcSR.getJDBCResource()
		theJDBCResource.setName(dsName)
    		
		print "Set JDBC Connection Pool Parameters"
		connectionPoolParams = theJDBCResource.getJDBCConnectionPoolParams()
		connectionPoolParams.setConnectionReserveTimeoutSeconds(int(props.getProperty("ConnectionReserveTimeoutSeconds")))
		connectionPoolParams.setMaxCapacity(int(props.getProperty("MaxCapacity")))
		connectionPoolParams.setTestTableName(props.getProperty("TestTableName"))
    		
		print "Set JDBC Data Resource Parameters"
		dsParams = theJDBCResource.getJDBCDataSourceParams()
		dsParams.addJNDIName(props.getProperty("JNDIName"))

		print "Set JDBC Driver Parameters"
		driverParams = theJDBCResource.getJDBCDriverParams()
		driverParams.setUrl(props.getProperty("Url"))
		driverParams.setDriverName(props.getProperty("DriverName"))
    		
		driverParams.setPassword(props.getProperty("Password"))
		driverProperties = driverParams.getProperties()
		user = driverProperties.createProperty("user")
		user.setValue(props.getProperty("User"))
    		
		dbname = driverProperties.createProperty("DatabaseName")
		dbname.setValue(props.getProperty("DatabaseName"))
    		
		targets = props.getProperty("Targets")
		addTargets(jdbcSR, targets)
					
def deployLibraries():
	print "Deploying libraries"
	pathList = getPropertyPathList("libraries")
	for path in pathList:
		props = loadProps(path)
			
		libraryName = props.getProperty("Name")
		libraryPath = props.getProperty("Path")
		print "Deploy library " + libraryName +":"+ libraryPath
		
		targets = props.getProperty("Targets")
		deploy(libraryName,libraryPath, targets, "true") 
		
def deployApplications():
	print "Deploying Applications"
	pathList = getPropertyPathList("applications")
	for path in pathList:
		props = loadProps(path)
			
		appName = props.getProperty("Name")
		appPath = props.getProperty("Path")
		print "Deploy application " + appName +":"+ appPath
		
		targets = props.getProperty("Targets")
		deploy(appName,appPath, targets) 

print "Start configuring Domain"

print "Connect to ${WLS_URL} as user ${WLS_USER}"
connect("${WLS_USER}","${WLS_PW}", "${WLS_URL}")
edit()

startEdit()
try:
	configureClusters()
	configureJdbcSystemResources()
	#configureFileStores()
	configureJdbcStores()
	configureJmsServers()
	
	configureJmsSystemResources()
	configureJmsConnectionFactories()
	configureDistributedQueues()
	configureDistributedTopics()
	
	#configureJmsSubDeployments()
	#configureQueues()
	#configureTopics()
	
	deployLibraries()
	deployApplications()

	save()
	activate(block="true")
	print "Domain configuration completed successfully"
except:
	dumpStack()
	print "Aborting domain configuration due to errors!"
	stopEdit('y')

