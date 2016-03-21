### Apache Tomcat Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component and Stack for Apache Tomcat cluster, or stand alone server.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/Apache-Tomcat` build template. 

### Customizing the Pattern
--------------------------------------

* The SSL related key store files can be added under `Tomcat/content/conf` folder, replacing the default SSL key store files
* Any custom Silver Fabric Jython Component scripts can be added under `Tomcat/scripts` folder
* Any Silver Fabric `configure.xml` rules (see [TIBCO Silver Fabric Developer's Guide]) can be added in `Tomcat/configure/configure.xml`

### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric Tomcat Enabler].

### Build Steps
--------------------------------------
1. Under `Tomcat` sub-folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
	* Verify and set enabler information in `build.properties`. If your Enabler version is different, update the Enabler version.
2. Under `Tomcat`  sub-folder, for every Tomcat Component you need, create a file `build-xxx.properties`, for example, `build-clusterl1.properties`
3. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
5. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[TIBCO Silver Fabric Tomcat Enabler]: <https://docs.tibco.com/pub/silver_fabric_tomcat/5.6.0/TIB_silver_fabric_5.6.0_tomcat_enabler_guide.pdf>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>