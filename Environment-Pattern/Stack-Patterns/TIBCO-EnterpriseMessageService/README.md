### TIBCO Enterprise Message Service Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component and Stack for TIBCO Enterprise Message Service server in 
fault-tolerant setup of an active-passive pair..

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/TIBCO-EnterpriseMessageService` build template. 
### Customizing the Pattern
--------------------------------------

* Any custom Silver Fabric Jython Component scripts can be added under `EMS/scripts` folder
* Any Silver Fabric `configure.xml` rules (see [TIBCO Silver Fabric Developer's Guide]) can be added in `EMS/configure/configure.xml`


### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric Enabler for TIBCO Enterprise Message Service].

### Steps
--------------------------------------
1. Under `EMS`  sub-folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
2. Under `EMS`  sub-folder, for every Enterprise Message Service fault-tolerant Component you need, create a file named with the format `build-xxx.properties`, for example, `build-emsft1.properties`
3. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
5. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[TIBCO Silver Fabric Enabler for TIBCO Enterprise Message Service]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-tibco-enterprise-message-service-2-1-0>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>