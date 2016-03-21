### TIBCO BusinessWorks 6 with TEA Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Components and Stacks for TIBCO BusinessWoks 6 Domain that comprises of 
TIBCO Enterprise Message Service, MySQL database, TIBCO Enterprise Administrator and TIBCO BusinessWorks 6 machines.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/TIBCO-EnterpriseMessageService`,  
`Build-Templates/TIBCO-BusinessWorks6` and `Build-Templates/MySQL-CE`.

### TIBCO Silver Fabric Enablers
-------------------------------------------------

This Stack pattern uses following Enablers:

 * [TIBCO Silver Fabric Enabler for TIBCO Enterprise Message Service]
 * [TIBCO Silver Fabric Enabler for TIBCO Enterprise Administrator]
 * TIBCO Silver Fabric Enabler for MySQL Community Edition] 
 * [TIBCO Silver Fabric Enabler for ActiveMatrix BusinessWorks]

### Download MySQL JDBC Driver
--------------------------------------------
[Download MySQL Connector/J] latest MySQL JDBC driver and install it under `BusinessWorks6/content/jdbc`

### Steps
--------------------------------------
1. Under pattern folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
2. Under `BusinessWorks6`  sub-folder, for every BusinessWorks  machine you need, create a file named with the format `build-xxx.properties`, for example, `build-bw6-1.properties`. 
3. Under `BusinessWorks6`  sub-folder, in each `build-xxx.properties` file, set JDBC driver file property to the version you down loaded, for example:
	* bw6.contextvar.bw6.jdbc.driver.file=/jdbc/mysql-connector-java-5.1.36-bin.jar`
4. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
5. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
6. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[TIBCO Silver Fabric Enabler for TIBCO Enterprise Administrator]: <https://docs.tibco.com/pub/sfte/1.0.0/doc/pdf/TIB_sfte_1.0_users_guide.pdf>
[TIBCO Silver Fabric Enabler for TIBCO Enterprise Message Service]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-tibco-enterprise-message-service-2-1-0>
[TIBCO Silver Fabric Enabler for ActiveMatrix BusinessWorks]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-activematrix-businessworks-3-1-0>
[TIBCO Silver Fabric Enabler for MySql Community Edition]: <https://github.com/fabrician/mysql-ce-enabler>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>