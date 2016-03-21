### Oracle WebLogic 12.1.3 Server Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component and Stack for Oracle WebLogic 12.1.3 stand alone server..

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/OracleWebLogic/Server` build template. 


### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric Enabler for BEA WebLogic].

### Pattern Customization
-------------------------------------
* SSL related Java keystore files are under `WebLogic-Server/content/keystores` 
* Add custom jar files under `WebLogic-Server/content/domain_home/lib` 
* Add  any Domain Home files under `WebLogic-Server/content/domain_home`: You may create sub-folders, if needed
* WebLogic Home files under `WebLogic-Server/wl_home`: You may create sub-folders, if needed.

### Steps
--------------------------------------
1. Under `WebLogic-Server` sub-folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
2. Under `WebLogic-Server` sub-folder, for every WebLogic-Server Component you need, create a file named with the format `build-xxx.properties`, for example, `build-server1.properties`
3. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
5. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[TIBCO Silver Fabric Enabler for BEA WebLogic].: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-bea-weblogic-5-6-0>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>