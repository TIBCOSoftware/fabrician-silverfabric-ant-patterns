### TIBCO BusinessEvents Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component for TIBCO BusinessEvents machines without TRA.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/TIBCO-BusinessEvents` build template. 

### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric Enabler for TIBCO BusinessEvents].

### Steps
--------------------------------------
1. Under `BusinessEvents`  sub-folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
	* Verify and set enabler information in `build.properties`. If your Enabler version is different, update the Enabler version.
2. Under `BusinessEvents`  sub-folder, for every BusinessEvents Component you need, create a file named with the format `build-xxx.properties`, for example, `build-tlm1.properties`
3. Customize any Component specific properties in the `build-xxx.properties file`. BusinessEvents Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target
5. To understand the meaning of the properties specified in Enabler specific property files, please consult Enabler documentation. 
Please note that the properties defined in the Enabler property files are inputs to Component Ant build files.

[TIBCO Silver Fabric Enabler for TIBCO BusinessEvents]:<https://docs.tibco.com/pub/sfbe/3.1.0/doc/pdf/TIB_sfbe_3.1_users_guide.pdf>
[TIBCO Silver Fabric Enabler for BusinessEvents Enterprise Edition]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-activespaces-enterprise-edition-1-0-1>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>