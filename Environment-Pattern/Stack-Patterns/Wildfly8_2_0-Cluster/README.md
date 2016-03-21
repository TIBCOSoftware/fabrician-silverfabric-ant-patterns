### WildFly 8.2.0 Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component and Stack for TIBCO WildFly 8.2.0 cluster, or stand alone server.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/WildFly8_2_0` build template. 

### Customizing the Pattern
--------------------------------------

* The SSL related key store files can be added under `WildFly/content/conf` folder, replacing the default SSL key store files
* Any custom Silver Fabric Jython Component scripts can be added under `WildFly/scripts` folder
* Any Silver Fabric `configure.xml` rules (see [TIBCO Silver Fabric Developer's Guide]) can be added in `WildFly/configure/configure.xml`


### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric WildFly/JBoss Enabler].

### Silver Fabric Variable Provider
---------------------------------------------------

This pattern uses a Silver Fabric variable provider named `GlobalVariableProvider`. 
The `GlobalVariableProvider` variables are used in `WildFly/configure/configure.xml` file and provide connection
information for a MySQL database. If you do not have access to a Silver Fabric variable provider, 
you may hard code relevant values in `WildFly/configure/configure.xml`.

### Download MySQL JDBC Driver
--------------------------------------------
[Download MySQL Connector/J] (5.1.21 or later version) MySQL JDBC driver and install it under
`WildFly/content/wildfly/modules/system/layers/base/mysql/main` folder. Replace `mysql-connector-java-5.1.21-bin.jar` in  `WildFly/content/wildfly/modules/system/layers/base/mysql/main/module.xml`
with the name of your MySQL JDBC driver jar file.

### Steps
--------------------------------------
1. Under `WildFly`  sub-folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
2. Under `WildFly`  sub-folder, for every WildFly Component you need, create a file named with the format `build-xxx.properties`, for example, `build-cluster1.properties`
3. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
5. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[ TIBCO Silver Fabric WildFly/JBoss Enabler]: <https://docs.tibco.com/pub/silver_fabric_enabler_redhat_JBoss/5.6.0/pdf/TIB_silver_fabric_5.6.0_JBoss_enabler_guide.pdf>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>
[Download MySQL Connector/J]: <https://dev.mysql.com/downloads/connector/j/>