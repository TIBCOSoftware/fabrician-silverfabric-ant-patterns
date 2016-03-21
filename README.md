### TIBCO Silver Fabric Ant Patterns

### Introduction
--------------------------------------
This Eclipse project assumes you are familiar with [TIBCO Silver Fabric Concepts].

TIBCO Silver Fabric Ant Patterns can be used to build TIBCO Silver Fabric Components and Stacks, and manage
continuous deployment of archives into running Components.

Beside using the Ant patterns defined in this project, there are two other viable alternatives for building TIBCO Silver Fabric  
Components and Stacks and managing continuous deployment of archives into running Components:

1. Use TIBCO Silver Fabric Administrator web user interface (UI) to create Stacks and Components: This approach is recommended if you are new to TIBCO Silver Fabric. See [TIBCO Silver Fabric Cloud Administration Guide] for details on how to use the UI to create Components and Stacks.
2. Use TIBCO Silver Fabric Administrator REST API: This approach is recommended if you want to integrate TIBCO Silver Fabric with custom REST API client, or if you want to manage continuous deployment of archives into running Components without the use of Ant.

### Generating Ant Build Packages
-----------------------------------------------

Once you have built a Silver Fabric Stack using any method, you can automatically  generate Ant build packages for the Stack and its Components using Silver Fabric Manager (UI). See [TIBCO Silver Fabric Cloud Administration Guide], 
**Packaging Stacks for Ant Task Deployment** for details on how to generate an Ant package for a Stack and its Components created through the UI. 

These generated Ant packages can be used directly, or they can be customized  to define new build templates and patterns. In fact,
this is how the build templates and patterns included in this project were created. 

### Silver Fabric Version
---------------------------------
These patterns have been tested with TIBCO Silver Fabric version 5.7.1, but are expected to work with TIBCO Silver Fabric versions 5.6.0 or later.

### Key Concepts
--------------------------------------
To use these patterns, it helps to understand following concepts:

* Apache Ant
* Build Templates
* Environment Pattern
* Stack Patterns
* Archive Deployment Patterns

[Apache Ant] is a general purpose Java based build tool with a built-in set of core build tasks. Core Ant task set can be extended to include custom Ant tasks. 
TIBCO Silver Fabric provides a library of custom Ant tasks that are used in this project. [TIBCO Silver Fabric Developer's Guide] is a good reference for Silver Fabric custom Ant tasks. 

In order to enable the use of Silver Fabric custom Ant tasks, download `Admin/Downloads/SilverFabricCLI.tar.gz`  from Silver Fabric Manager UI, extract the tar to any folder on the build machine, and set 
**Ant Home** to the absolute path of the extracted `SilverFabricCLI` folder. If you are using Eclipse with this project, Ant Home can be set under 
`Eclipse>Preferences...`. 

*Build Templates* consist of Ant build files for building various types of Silver Fabric Components and Stacks, and 
for deploying archives to various running Components. 

*Environment Pattern*  can be used to define a new Silver Fabric environment.  Each *Environment Pattern* contains a set of *Stack Patterns*, *Archive Deployment Patterns* and an environment  
specific top-level `build.properties` file that specifies, among other things, the connection infromation for a Silver Fabric Manager.

*Stack Patterns*  under the *Environment Pattern* are used for building a set of Components and Stacks, for example  `Environment-Pattern/Stack-Patterns/Apache-Tomcat-Cluster` 
pattern is used to build Apache Tomcat related Components and Stacks. Some *Stack Patterns* are simple in that they define one Stack with a single Component. Other *Stack Patterns* are complex
in that they define multiple Stacks and Components. Typically, Stack patterns define each Stack to include a single Component, although that is not required.

*Archive Deployment Patterns* under *Environment Pattern* are used to `deploy`, `undeploy`, `start` and `stop` various application archives into 
running targeted Components using Silver Fabric Continuous Deployment  Ant tasks. 

### Project Directory Structure
-----------------------------------------

The project directory structure is as follows:

* `ant.lib` folder contains some open source Ant contributed custom tasks, which should not be confused with Silver Fabric Ant custom tasks
* `ssl` folder  contains SSL trust store file for HTTPS communications with Silver Fabric manager
* `build.properties` file at the project top-level  defines project specific Ant build properties pertaining to directory structure of the project
* `Build-Templates` folder contains build templates for various Silver Fabric Enablers. 
Each build template folder contains one or more files for building Components for a specific Enabler and a singleton Stack that includes a single Component. 
* `Environment-Pattern` folder contains an environment specific `build.properties` file and `Stack-Patterns`
* `Environment-Pattern/Stack-Patterns` folder contains a set of patterns for building  Silver Fabric Components and Stacks. 
Each *Stack Pattern* folder contains one or more Enabler specific sub-folders.  
* `Environment-Pattern/ArchiveDeployment-Patterns` folder contains patterns for continuous deployment of application archives to running Components


### How Stack Patterns Ant Build Works
---------------------------------------------------

The Ant build process for each `Stack Pattern` works as follows:

1. The top-level `build.xml` under each *Stack Pattern* invokes  `Build-Templates/Stack-Build/build-pattern.xml` Ant build file
2. The `build-pattern.xml` invokes sibling `build-components.xml` and `build-stacks.xml` Ant build files
to build required Components and Stacks, respectively.
3. The `build-components.xml` file invokes target Component Ant build file. For example, if the 
build template is Apache Tomcat, the target Component Ant build file is  `Build-Templates/Apache-Tomcat/build-component.xml`. 
The target Component Ant build file is specified in *Stack Pattern's*  Enabler specific `build.properties` file using `component.build.xml` property.
4. The `Build-Templates/Stack-Build/build-stacks.xml` file invokes the target Stack Ant build file. For example, if the
build template is Apache Tomcat, the target Stack Ant build file is `Build-Templates/Apache-Tomcat/build-stack.xml`. The target Stack Ant build file
is specified in *Stack Pattern's*  Enabler specific `build.properties` file using `stack.build.xml` property.
 
### How Archive Deployment Patterns Ant Build Works
----------------------------------------------------------------------

The Ant build process for each `Archive Deployment Pattern` works as follows:

1. The top-level `build.xml` under each *Archive Deployment Pattern* invokes  `Build-Templates/ArchiveDeployment-Build/build-deploy-pattern.xml` Ant build file
2. The `build-deploy-pattern.xml` invokes sibling `build-deploy-archives.xml` Ant build file
3. For each deployment target criteria file found in the pattern, `build-deploy-archives.xml` file invokes sibling `build-deploy-archive.xml` file. 
 
In the next section, we will describe the steps to define  a new Silver Fabric Environment.

### Defining a New Silver Fabric Environment
---------------------------------------------------------
 
Below are the steps for creating a new Silver Fabric environment:

1. If your Silver Fabric Manager is SSL enabled, copy the SSL trust store file to the `ssl` folder under the project folder. The default trust store file, `ssl.keystore`, is already included in the `ssl` folder.
2. Edit the top-level `build.properties` file under the project folder to set appropriate values for:
	* `trustfile` property (default is already set)
	* `trustpassword` property (default is already set)
3. Create a new  folder under the project folder, named for the environment, for example, `dev`. 
2. Copy the `build.properties` file from `Environment-Pattern` folder to the new environment folder, for example `dev` folder, and set following properties in it:
	* `sf.url` should be set  to Silver Fabric Manger URL, e.g. http://broker:8000, or https://broker:8443
	* `sf.user` should be set to a user that has permission to build Silver Fabric Components and stacks
	* `sf.password` should be set to the Silver Fabric password for `sf.user`
	* `environment.name` should be set to this environment name, for example, `dev`
	* `shared.dir` should be set to a NFS4 network file system mount point that is available on all Silver Fabric Engine hosts
	* Other properties should be set in this file, if applicable, but typically are not needed
3. Copy any Stack or Archive Deployment pattern to `dev` folder and give it a name that reflects the pattern release version, for example, Apache-Tomcat-Cluster-1.0
4. Go under the new pattern release folder, read the `README.md` file and follow the steps noted in the README.md file.

### Adding New Build Template
-------------------------------------------------------------

if you want to add new build templates, create a sub-folder under `Build-Templates` folder. In the new build template folder, define required
Component and Stack Ant build files.You may define multiple Component and Stack Ant build files applicable to different use cases.
The most common way to define new build files is to define Components and Stacks using Silver Fabric Manager UI, generate Ant package
for the Stack, extract build files from the stack and customize them as needed.

### Adding New Stack Pattern
-------------------------------------------------------------

if you want to add new Stack patterns, create a new sub-folder under `Environment-Pattern/Stack-Patterns`. Under the new pattern 
 folder, add an optional  `build.properties` for defining any common properties at the pattern level. Add boilerplate pattern
top-level `build.xml` file: it is same for every pattern, so you can copy it from any existing pattern.

Under the pattern folder, create a sub-folder for each Enabler type used in the pattern. Under the Enabler sub-folder, create a top-level
Enabler specific `build.properties` file. For each Component you need to build for a given Enabler type, add a new Component specific `build-xxx.properties` file, whereby the
`xxx` can be any name.  In the Component specific`build-xxx.properties` file, specify properties relevant to the specific Component. 

### Build Timeout
--------------------------

If you are working over a slow network connections between your build machine and TIBCO Silver Fabric Manager host,
you may get `wink` client timeouts. You can disable `wink` client timeout by using following Java system property with your
Ant build command:

* `-Dwink.client.readTimeout=0`

[Apache Ant]:<http://ant.apache.org>
[TIBCO Silver Fabric Concepts]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_concepts.pdf>
[TIBCO Silver Fabric Developer's Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_developers_guide.pdf>
[TIBCO Silver Fabric Cloud Administration Guide]:<https://docs.tibco.com/pub/silver_fabric/5.7.1/doc/pdf/TIB_silver_fabric_5.7.1_cloud_administration.pdf>