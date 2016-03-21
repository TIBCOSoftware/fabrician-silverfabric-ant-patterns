### MySQL Community Edition Database Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component and Stack for MySQL Community Edition database.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/MySQL-CE` build template. 

### Customizing the Pattern
--------------------------------------

* Custom SQL files can be added under `MySQL/content/sql` folder: The `secure-db.sql` in this folder file secures the database
* Any custom Silver Fabric Jython Component scripts can be added under `MySQL/scripts` folder
* Any Silver Fabric `configure.xml` rules (see [TIBCO Silver Fabric Developer's Guide]) can be added in `MySQL/configure/configure.xml`

### Enabler
--------------------------------

This Stack pattern uses [MySQL Community Edition Enabler].

### Steps
--------------------------------------
1. Under `MySQL`  sub-folder, in  `build.properties` file:
	* Set `release.version` property to match your release version
	* Verify and set enabler information in `build.properties`. If your Enabler version is different, update the Enabler version.
2. Under `MySQL`  sub-folder, for every MySQL Component you need, create a file named with the format `build-xxx.properties`, for example, `build-mysql1.properties`
3. Customize any Component specific properties in the `build-xxx.properties file`. Component name  must be unique within a given Silver Fabric environment.
4. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
5. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[MySql Community Edition Enabler]: <https://github.com/fabrician/mysql-ce-enabler>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>