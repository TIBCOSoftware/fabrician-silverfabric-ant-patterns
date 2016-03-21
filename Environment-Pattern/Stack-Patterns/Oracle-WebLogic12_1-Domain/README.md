### Oracle WebLogic 12.1.3 Domain Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to build TIBCO Silver Fabric Component and Stack for Oracle WebLogic 12.1.3 Domain
comprising of 2 JMS servers, 1 JMS cluster, and 1 application server cluster. 

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/OracleWebLogic/Admin` and
. `Build-Templates/OracleWebLogic/Cluster` build templates.

### TIBCO Silver Fabric Enabler
------------------------------------------

This Stack pattern uses [TIBCO Silver Fabric Enabler for BEA WebLogic].

### Pattern Customization
-------------------------------------
* SSL related Java keystore files are under `WebLogic-Admin/content/keystores`  and `WebLogic-Cluster/content/keystores`
* Add custom jar files under `WebLogic-Admin/content/DOMAIN_HOME/lib` and `WebLogic-Cluster/content/DOMAIN_HOME/lib` 
* Add  any Domain Home files under `WebLogic-Admin/content/DOMAIN_HOME` and `WebLogic-Cluster/content/DOMAIN_HOME: You may create sub-folders, if needed
* WebLogic Home files under `WebLogic-Admin/WL_HOME` and `WebLogic-Cluster/WL_HOME: You may create sub-folders, if needed.
* There is a custom Silver Fabric script under `WebLogic-Admin/scripts`  named `WlsAdmin.py` used to configure the domain 
* There is a custom Silver Fabric script under under `WebLogic-Cluster/scripts`  named `WlsCluster.py` used to configure the cluster 


### Steps
--------------------------------------
1. Under pattern folder,  in  `build.properties` file:
	* Set `release.version` property to match your release version
2. * In `WebLogic-Admin/content/config/jdbc-system-resources/jdbc-system-resourcesN`.properties` set Oracle database connection information for JDBC stores
3. Use the `build.xml` under the pattern folder to build desired Ant target: `release` or `clean`
4. To understand the meaning of the properties specified in specific property files, please consult Enabler documentation. 
Please note that the properties defined in the  property files are inputs to Component and Stack Ant build files.

[TIBCO Silver Fabric Enabler for BEA WebLogic].: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-bea-weblogic-5-6-0>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>