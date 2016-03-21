### Oracle WebLogic Domain Deployment Pattern

### Introduction
--------------------------------------
This Stack pattern can be used to deploy, start, stop and un-deploy archives into running Oracle WebLogic Domain clusters.

### Build Template
--------------------------

This pattern uses Component and Stack Ant build files found under  `Build-Templates/ArchiveDeployment-Build` template. This pattern is 
an example. The Ear file in this pattern is an example application.

### Property Files
-----------------------------

The `target-criteria.properties` file identifies the `deploy` and `start` target. The `stop-criteria.properties` identifies `stop` and
`undeploy` target. The two criteria files may not be symmetrical. For example, in WebLogic Domain, the `deploy`  and `start` target is WebLogic Domain Admin and the `undeploy` and `stop` target
is a specific cluster in the Domain.

The `build.properties` file is used by Ant build files. The `deploy.properties` file  contains Continuous Deployment properties. See 
*Deploying Archives with Continuous Deployment* in the [TIBCO Silver Fabric Cloud Administration Guide] for details on
Continuous Deployment properties.

### Build Steps
--------------------------------------
1. Rename `rubis` folder to your application name
2. Replace the `rubis.ear` archive file with your application archive file
3. Customize properties files under the application name sub-folder as applicable. (See [TIBCO Silver Fabric Developer's Guide]) for details on Continuous Deployment properties files.
4. (Optional) Build `repo` target to publish archive to an archive repository configured with your TIBCO Silver Fabric Manager
5. Build `deploy-repo` to deploy archive from repository to target cluster. Alternatively, you can use `deploy` target, if you skipped step 4.
6. Build `start` target to start the archive.
7. Build `stop` target to stop the archive
8. Build `undeploy` target to undeploy the archive

[TIBCO Silver Fabric Enabler for BEA WebLogic].: <https://docs.tibco.com/products/tibco-silver-fabric-enabler-for-bea-weblogic-5-6-0>
[TIBCO Silver Fabric Cloud Administration Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_cloud_administration.pdf>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>