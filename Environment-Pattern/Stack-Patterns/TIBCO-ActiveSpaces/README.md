### TIBCO ActiveSpaces Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component for TIBCO ActiveSpaces Meta-space cluster.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/TIBCO-ActiveSpaces` build template. 


### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric Enabler for ActiveSpaces Enterprise Edition].

### Steps
--------------------------------------
1. Under `ActiveSpaces` sub-folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
	* Verify and set enabler information in `build.properties`. If your Enabler version is different, update the Enabler version.
2. Under `ActiveSpaces` sub-folder, for every ActiveSpaces Component you need, create a file named with the format `build-xxx.properties`, for example, `build-ms1.properties`. Each
Component corresponds to an ActiveSpaces Meta-space cluster.
3. Customize any Component specific properties in the `build-xxx.properties file`. ActiveSpaces Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target
5. To understand the meaning of the properties specified in Enabler specific property files, please consult Enabler documentation. 
Please note that the properties defined in the Enabler property files are inputs to Component Ant build files.

[TIBCO Silver Fabric Enabler for ActiveSpaces Enterprise Edition]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-activespaces-enterprise-edition-1-0-1>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>