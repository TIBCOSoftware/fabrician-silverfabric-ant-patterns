### TIBCO TRA Domain Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Components and Stacks for a TIBCO TRA Domain comprising of 
TIBCO Enterprise Message Service, TIBCO Administrator and TIBCO Logical Machines (TLM). This pattern assumes an external
Oracle database is used for TIBCO TRA Domain repository.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/TIBCO-EnterpriseMessageService`,  
, `Build-Templates/TIBCO-Administrator` and `Build-Templates/TIBCO-BusinessWorks5`.

### TIBCO Silver Fabric Enablers
--------------------------------------------

This Stack pattern uses following enablers:

	* [TIBCO Silver Fabric Enabler for TIBCO Enterprise Message Service]
	* [TIBCO Silver Fabric Enabler for ActiveMatrix BusinessWorks]
	* [TIBCO Silver Fabric Enabler for TIBCO Administrator]

### Download Oracle Database 11g Release 2 JDBC Drivers
------------------------------------------------------------------------------
[Download Oracle Database 11g Release 2 JDBC Drivers] `odjbc6.jar` driver and install it under `BusinessWorks5/content/jdbc` 
and `Administrator/content/jdbc` folders.

### TIBCO Administrator Enabler Fault-Tolerant Option
-------------------------------------------------------------

This pattern uses [TIBCO Silver Fabric Enabler for TIBCO Administrator] *Fault tolerant option*. This means TIBCO Administrator log 
files and other configuration files are stored on a shared file system. 

### TIBCO BusinessWorks Enabler Fast TLM Option
------------------------------------------------------------------

This pattern uses [TIBCO Silver Fabric Enabler for ActiveMatrix BusinessWorks] *Fast TLM option*. This means TIBCO BusinessWorks log 
files and other configuration files are stored on a shared file system. Also, BusinessWorks local application deployments 
are pushed to the shared file system.

### Steps
--------------------------------------
1. Under pattern folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
2. Under `Administrator` sub-folder, in `build-admin1.properties`, set database conenction properties
		* `jdbc.driver`
		* `db.url`
		* `db.user`
		* `db.password`
2. Under `BusinessWorks5`  sub-folder, for every BusinessWorks logical machine you need, create a file named with the format `build-xxx.properties`, for example, `build-tlm1.properties`. 
3. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
5. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[Download Oracle Database 11g Release 2 JDBC Drivers] : <http://www.oracle.com/technetwork/apps-tech/jdbc-112010-090769.html>
[TIBCO Silver Fabric Enabler for TIBCO Enterprise Message Service]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-tibco-enterprise-message-service-2-1-0>
[TIBCO Silver Fabric Enabler for ActiveMatrix BusinessWorks]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-activematrix-businessworks-3-1-0>
[[TIBCO Silver Fabric Enabler for TIBCO Administrator]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-tibco-administrator-enterprise-edition-2-9-0>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>