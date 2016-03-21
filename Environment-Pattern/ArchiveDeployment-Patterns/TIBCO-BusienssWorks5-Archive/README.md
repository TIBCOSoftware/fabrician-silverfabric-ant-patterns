### TIBCO BusinessWorks 5 Deployment Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to deploy, start, stop and un-deploy archives into running TIBCO BusinessWorks 5 logical machines.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/ArchiveDeployment-Build` template. This pattern is 
an example. The Ear file in this pattern is an example application.

### Property Files
-----------------------------

The `target-criteria.properties` file identifies the `deploy` and `start` target. The `stop-criteria.properties` identifies `stop` and
`undeploy` target. In this pattern, the two criteria files are symmetrical, but nevertheless, two separate files are required.

The `build.properties` file is used by Ant build files. The `deploy.properties` file  contains Continuous Deployment properties. See 
*Deploying Archives with Continuous Deployment* in the [TIBCO Silver Fabric Cloud Administration Guide] for details on
Continuous Deployment properties.


### Assumptions
----------------------------

This example assumes you are using a Silver Fabric dynamic variable porvider named GlobalVariablePorvider. If you are not using
such a  dynamic variable provider, remove `VariableProvider=GlobalVariableProvider` entry from `wsdemo2/deploy.properties` file.
In that case, you may specify your global variables in the `deploy.properties` file as discussed in the [TIBCO Silver Fabric Enabler for ActiveMatrix BusinessWorks] guide.

### Build Steps
--------------------------------------
1. Rename `wsdemo2` folder to your application name
2. Replace the `wsdemo2.ear` archive file with your application archive file
3. Customize properties files under the application name sub-folder as applicable. (See [TIBCO Silver Fabric Developer's Guide]) for details on Continuous Deployment properties files.
4. (Optional) Build `repo` target to publish archive to an archive repository configured with your TIBCO Silver Fabric Manager
5. Build `deploy-repo` to deploy archive from repository to target server. Alternatively, you can use `deploy` target, if you skipped step 4.
6. Build `start` target to start the archive.
7. Build `stop` target to stop the archive
8. Build `undeploy` target to undeploy the archive

[TIBCO Silver Fabric Enabler for ActiveMatrix BusinessWorks]: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-activematrix-businessworks-3-1-0>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>