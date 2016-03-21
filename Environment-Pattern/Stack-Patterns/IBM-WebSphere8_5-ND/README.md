### IBM WebSphere 8.5 Network Deployment Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Components and Stacks for BM WebSphere 8.5 Network Deployment cell.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/IBM-WebSphere` build template. 

### Customizing the Pattern
--------------------------------------

* The SSL related key store files can be added under `WebSphere-DM/content/conf` and `WebSphere-Cluster/content/conf` folders, replacing the default SSL key store files
* Any custom Silver Fabric Jython Component scripts can be added under `WebSphere-DM/content/script` and `WebSphere-Cluster/content/script` folders
* Any Silver Fabric `configure.xml` rules (see [TIBCO Silver Fabric Developer's Guide]) can be added in `WebSphere-DM/configure/configure.xml` and `WebSphere-Cluster/configure/configure.xml` files


### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric Enabler for IBM WebSphere].

### Build Steps
--------------------------------------
1. Under pattern folder,  `build.properties` file:
	* Set `release.version` property to match your release version
	* Verify and set enabler information in `build.properties`. If your Enabler version is different, update the Enabler version.
2. Under `WebSphere-Cluster`  sub-folder, for every WebSphere cluster Component you need, create a file `build-xxx.properties`, for example, `build-clusterl1.properties`
3. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
5. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.
6. The Deployment Manager Stack must be started before or at the same time as the Cluster Stack.

[TIBCO Silver Fabric Enabler for IBM WebSphere]:<https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-ibm-websphere-5-6-0>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>