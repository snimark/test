{ "title": "VanTam Tool Deployment Parameters schema", "Description":
"Parameters use to deploy application in AWS",
"$schema": "http://json-schema.org/draft-04/schema#",  "type": "object",  "properties": {  "AppName": {  "type": "string",  "minLength": 3,  "description":"[Application] Name of the application. This value will be used to create other parameters such as StackName and values for New Relic and Sumo Logic."  },  "DNSName": {  "type": "string",  "minLength": 3,  "description": "[Application] Value used for setting up the DNS entry in Route 53 as the domain name for the application."  },  "Healthcheck": {  "type": "string",  "pattern": "(?:(tcp|http):(\\d+)(\\/.*)?)",  "description": "[Application] The value defines several pieces of the health check ping: protocol, port, and uri. Examples include: http:8080/health-check, tcp:22. The first example uses port 8080 over the HTTP protocol to hit the web page of www.example.com/health-check. The second example checks for an acknowledgment on port 22 over the TCP protocol.The port value should match the listening port of the application. That is, if the app is configured to listen on port 8082, then the port value should match."  },  "Platform": {  "enum": ["jboss5", "jboss6", "dropwizard", "angular", "tomcat", "springboot"],  "description":"[Application] This important parameter will decide in which platform the application will be deployed."  },  "TagBusUnit": {  "enum": ["mcd", "media", "content-delivery", "contentdelivery", "automation"],  "description": "[Application] Indicates which group manages the application. (Might still affect which account is billed in the budget.) This value will also be used to determine which engineering team identifier is added to the SNS topic created for the application."  },  "TagEnv": {  "enum": ["dev", "int", "qa", "prod"],  "description": "[Application] One of four environments should be set for this parameter. This value along with Platform are vital to the which system parameters are used in standing up the infrastructure for the application's deployment."  },  "TagOwner": {  "type": "string",  "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,6}$",
"description": "\[Application\] Complete email address of the
development team responsible for the application. This address is also
attributed to the SNS topic created for the application. Alerts sent to
the topic are then sent to the contacts based on that email address." },
"TagProject": { "type": "string", "minLength": 2, "description" :
"\[Application\] An identifier to denote any group of applications or
project wiith which this application is associated." }, "TagOrigin": {
"type": "string", "default": "vantam", "description" : "\[Application\]
Vantam tag to identify applications deployed through pipeline or project
with which this application is associated." }, "AMImage": { "type":
"string", "pattern":
"\^ami-\[a-z0-9\]{8}$",  "description" : "[System] The id of the Amazon Image which is preconfigured with the system and puppet tools necessary to deploy the application. This value is now managed at the system level to avoid the need to keep up with which images have been upgraded or are out of date."  },  "Elbsubnet1": {  "type": "string",  "pattern": "^subnet-[a-z0-9]{8}$",
"description" : "\[System\] These are the subnet ids for the elastic
load balancer (ELB). The values currently are private subnets only.
Availability Zones are paired with subnets (one-to-one), meaning these
choices will also define the availability zones for the applications."
}, "Elbsubnet2": { "type": "string", "pattern":
"\^subnet-\[a-z0-9\]{8}$",  "description" : "[System] See Elbsubnet1"  },  "IAMRole": {  "type": "string",  "default": "ct-avail-ec2-role",  "description" : "[System] This is the Amazon Role name used when creating the EC2 instances. It is Amazon's method for granting permission to activities performed by the applications running on these EC2s. This provides the application privileges without managing a specific user account for resource access."},  "KeyName": {  "type": "string",  "minLength": 1,  "default" : "sni-enterprise: hybrid-d [dev, int, qa], hybrid-p [prod] sni-mcd: kpd16068 [dev], kpi16068 [int], kpq16182 [qa], kpp16182 [prod]",  "description" : "[System] The name of the SSH key allowing access to the EC2s. Amazon EC2s are key-based system rather than password based systems."},  "Securitygrp": {  "type": "string",  "minLength": 8,  "default": "sni-enterprise: webserver-vpc-8180 [dev, int], all-sniqa-vpc [qa], webserver-vpc-8180 [prod] sni-mcd: dev-vpc-ssh,dev-web-private [dev], int-vpc-ssh,int-web-private [int], qa-vpc-ssh,qa-web-private [qa] prod-vpc-ssh,prod-web-private [prod]",  "description" : "[System] [Deprecated] Comma separated list of security groups identified by name applied to the EC2. The security groups acts as firewall with rules allowing IP and port access in both directions."  },  "Subnet1": {  "type": "string",  "pattern": "^subnet-[a-z0-9]{8}$",
"default" : "sni-enterprise: subnet-b9a390d4 \[dev, int\],
subnet-a04b60d4 \[qa\], subnet-4b90a326 \[prod\] sni-mcd:
subnet-bdef03e5 \[dev\], subnet-66ef033e \[int\], subnet-f55c6183
\[qa\], subnet-c9635ebf \[prod\]", "description" : "\[System\] These
subnet values are assigned to the Autoscaling Group (ASG) created as
part of the infrastructure. When EC2s are spun up by the ASG as the
CloudFormation template is executed, the networking is based on these
subnets for the IP addresses." }, "Subnet2": { "type": "string",
"pattern":
"\^subnet-\[a-z0-9\]{8}$",  "default" : "sni-enterprise: subnet-9ea390f3 [dev, int], subnet-3c730714 [qa], subnet-2190a34c [prod] sni-mcd: subnet-02c3dd29 [dev], subnet-46c2dc6d [int], subnet-c1ce8ceb [qa], subnet-20c88a0a [prod]",  "description" : "[System] See Subnet1"  },  "Domain": {  "type": "string",  "default" : "sni-enterprise: awsdev.snops.net [dev, int], awsqa.snops.net [qa], aws.snops.net [prod], sni-mcd: mcd.snidev [dev], mcd.sniint [int], mcd.sniqa [qa], mcd.sniprod [prod]",  "description" : "[System] Specify the hosted zone registered in Route 53."  },  "classes": {  "type": "array",  "items": {"enum" : ["tomcat_deploy", "sumo_deploy", "scalyr_deploy", "newrelic", "springboot_deploy", "jboss5_deploy", "jboss6_deploy", "drop_wizard_deploy", "dropwizard_deploy", "apache_app_deploy", "cloudwatch_logs", "timezone"]}, "minItems": 1,  "description" : "[System] The classes instruct which puppet scripting will be executed when the EC2s spin up. By default, all deployments will get newrelic scalyr_deploy and sumo_deploy to install the monitoring tools. The Platform app parameter provided by the app will define which deployment method will be executed for the application."  },  "AvailZone1": {  "type": "string",  "description" : "[Deprecated] Availability zone of Subnet1 (deduced)"  },  "AvailZone2": {  "type": "string",  "description" : "[Deprecated] Availability zone of Subnet2 (deduced)"  },  "AccountRoleArn": {  "type": "string",  "pattern": "^arn:aws:iam::[0-9]{12}:role\/mam-jenkins$",
"default" : "none", "description" : "\[Optional\] If a value is
provided, it will parse the AWS account number from the ARN and use
system values associated with that account. If omitted, it will use the
sni-enterprise\* system account values. Example:
arn:aws:iam::447434275168:role/mam-jenkins \[dev, int\]
arn:aws:iam::250312325083:role/mam-jenkins \[qa, prod\]" },
"CustomSecurityGroupSupport": { "type": "boolean", "default" : "none
(but treats as false)", "description" : "\[Optional\] If set to true
will create the custom security group named with pattern
{TagEnv}-{TagBusUnit}-{AppName} if doesn't already exist into the AWS
account and will add the EC2 instances created to that SecurityGroup.
Note: This custom security group has no specific Inbound/Outbound ports
open (require manual intervention)." }, "AlertSubscribers": { "type":
"array", "items": { "type": "string" }, "default": "none", "description"
: "\[Optional\] List of email addresses to subscribe to ELB alerts." },
"VantamPushNotificationServiceSupport": { "type" : "boolean", "default"
: "false", "description" : "\[Optional\] If set to true, will create a
SQS queue and will send throught it, VanTam application deployment
status events." }, "CertARN": { "title" : "AWS Certificate ARN", "type":
"string", "default" : "none", "description" : "\[Optional\] Sets the
certificate for SSL authentication when ElbFrontPort is set to 443 and
ElbProto is set to HTTPS. The certificate must be registered with the
AWS accounts and referenced via the ARN. Example value:
arn:aws:iam::344658159036:server-certificate/mamcloud-dev-interms1234"
}, "CustomELBPolicy": { "title" : "Custom ELB Policy", "type" :
"string", "default" : "DCI-ELBSecurityPolicy", "description" :
"\[Optional\] Sets the name of custom ELB security policy on a Load
Balancer when using a certificate for SSL authentication. Unless a need
for a name other than then default is necessary, it should not be
overridden. Note: When updating the custom policy for security matters,
the default value will receive those updates." }, "ConnTimeout": {
"type": "string", "pattern":
"[^1]{1,6}$",  "default" : "60",  "description" : "[Optional] Value in seconds for the idle connection timeout for ELBs."  },  "CrossZone": {  "enum": ["true", "false"],  "default" : "true",  "description" : "[Optional] Sets whether cross zone load balancing is enabled on the ELB. When enabled, load balancer nodes route traffic to the backend instances across all availability zones."  },  "ElbFrontPort": {  "type": "string",  "minLength": 2,  "default" : "80",  "description" : "[Optional] Port the ELB will listen for traffic for the applications. Set to 443 for SSL. If SSL, also set ElbProto and CernARN to SSL values.This value unless explicitly defined will assume the default value from the CloudFormation template. The healthcheck port number has no affect on this value."  },  "ElbPort": {  "type": "string",  "minLength": 2,  "default" : "8080",  "description" : "[Optional] Port the ELB will communicate with the EC2 instances. This value unless explicitly defined will assume the default value from the CloudFormation template. The healthcheck port number has no affect on this value."  },  "ElbProto": {  "enum": ["TCP", "HTTP", "HTTPS"],  "default" : "HTTP",  "description" : "[Optional] Communication protocol to the ELB. Set to HTTPS for SSL. If SSL, also set the ElbFrontPort and CernARN values to SSL values."  },  "ElbSubnetsType" : {  "enum" : ["public", "private"],  "default" : "None (but treats as 'private')",  "description" : "[Optional] If specified the list of subnet IDs (public or private) in the VPC will be attached to the load balancer. Note: if ElbSubnet1 & ElbSubnet2 are provided they will be used, and this 'ElbSubnetsType' will be ignored."  },  "InstProto": {  "enum": ["TCP", "HTTP", "HTTPS"],  "default" : "HTTP",  "description" : "[Optional] Communication protocol from the ELB to the EC2s."  },  "InstanceSize": {  "type": "string",  "minLength": 1,  "default": "t2.small",  "description" : "[Optional] Instance size for the EC2s spun up for the application."  },  "Minsize": {  "type": "string",  "pattern": "^[0-9]{1,4}$",
"default" : "1", "description" : "\[Optional\] Minimum number of EC2s to
be active for the application defined by the ASG." }, "Maxsize": {
"type": "string", "pattern":
"[^2]{1,4}$",  "default" : "3",  "description" : "[Optional] Maximum number of EC2s to be active for the application defined by the ASG."  },  "DesiredCapacity": {  "type": "string",  "pattern": "^[0-9]{1,4}$",
"default" : "1", "description" : "\[Optional\] Desired Capacity of EC2s
to be launched for the application defined by the ASG. If defined must
be lower or equal to Maxsize and cannot be lower than Minsize." },
"DeleteOldStacks": { "type": "string", "pattern": "[^3]{1}\$", "default"
: "1 \[dev\], 0 \[int, qa, prod\]", "description" : "\[Optional\]
Boolean value to inform whether old CloudFormation stacks for the
application should be deleted. 0 = No. 1 = Yes." }, "Snstopic": {
"type": "string", "minLength": 1, "description" : "\[Deprecated\] Sns
topic name used to receive CloudWatch notifications" }, "Sticky": {
"enum": \["YES", "NO"\], "default" : "NO", "description" : "\[Optional\]
Sets sessions to be sticky." }, "StackName": { "type": "string",
"minLength": 3, "default" : "sni-enterprise: {AppName}-{TagEnv}-\#
sni-mcd: {TagEnv}-{TagBusUnit}-{AppName}-\#", "description" :
"\[Optional\] Name of Cloud Formation Stack in AWS. " }, "app\_version":
{ "type": "string", "description" : "\[Optional\] Set from the --version
argument used when calling createStack.py. This value has always been
dynamically set by the createStack script." }, "EbsVolumeSize": {
"type": "integer", "default" : 8, "description": "\[Optional\] The EBS
volume size in GiB attached to the EC2 instance, allowed value from 1 to
16384." }, "timezone::zonefile" : { "type": "string", "default" :
"/usr/share/zoneinfo/UTC", "description" : "\[Optional\] Change the
timezone of your EC2 instance. Full path shall be provided. For this
parameter to be applied, 'timezone' in classes parameter shall be
present. For the list of possible timezones see:
https://www.archlinux.org/packages/core/any/tzdata/files/" },

        "EFSId": {
            "type": "string",
            "description": "Specify EFS ID for the EFS Volume you would like to use.  Leave the default if you do not wish to use an EFS Volume",
            "pattern": "^fs-[a-z0-9]*|none",
            "default": "none"
        },

        "MountPoint": {
            "type": "string",
            "description": "Full path and name of the mount point to use on EC2 instance when mounting EFS volume",
            "pattern": "^/[/a-zA-Z0-9]*",
            "default": "/var/data"
        },

        "AppLogDirectory": {
            "type": "string",
            "default" : "none",
            "description" : "[Centralized Monitoring & Logging] Application Log Directory to Clean Up"
        },
        "AppLogRetentionDays": {
            "type": "string",
            "default" : "7",
            "description" : "[Centralized Monitoring & Logging] Number of days to retain Application Logs"},

        "loggly::app_name": {
            "type": "string",
            "minLength": 3,
            "default" : "{AppName}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagEnv}"
        },
        "loggly::env": {
            "enum": ["dev", "int", "qa", "prod"],
            "default" : "{TagEnv}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagEnv}"
        },
        "newrelic::app_name": {
            "type": "string",
            "minLength": 3,
            "default" : "{AppName}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {AppName}"
        },
        "newrelic::env": {
            "enum": ["dev", "int", "qa", "prod"],
            "default" : "{TagEnv}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagEnv}."
        },
        "sumo_deploy::app_name": {
            "type": "string",
            "minLength": 3,
            "default" : "{AppName}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {AppName}"
        },
        "sumo_deploy::business_unit": {
            "type": "string",
            "default" : "{TagBusUnit}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagBusUnit}"
        },
        "sumo_deploy::container_type": {
            "type": "string",
            "default" : "{Platform},",
            "description" : "[Centralized Monitoring & Logging] Inherited from {Platform}"
        },
        "sumo_deploy::dev_team": {
            "type": "string",
            "default" : "{TagOwner}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagOwner}"
        },
        "sumo_deploy::sumo_env": {
            "enum": ["dev", "int", "qa", "prod"],
            "default" : "{TagEnv}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagEnv}"
        },
        "scalyr_deploy::scalyr_env": {
            "enum": ["dev", "int", "qa", "prod"],
            "default" : "{TagEnv}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagEnv}"
        },
        "scalyr_deploy::business_unit": {
            "type": "string",
            "default" : "{TagBusUnit}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {TagBusUnit}"
        },
        "scalyr_deploy::app_name": {
            "type": "string",
            "minLength": 3,
            "default" : "{AppName}",
            "description" : "[Centralized Monitoring & Logging] Inherited from {AppName}"
        },

        "AutoScaling": {
            "type": "object",
            "description" : "Please pick one way to scale below and include all the parameters under the 'AutoScaling' section of your parameters json file. The options to choose from are schedule based and cpu based scaling. The Type parameter is used to distinguish between the two options.",
            "properties": {
                "Type": {
                    "enum": ["scheduled", "cpu", "none"],
                    "default" : "none",
                    "description" : "Tells the automation to setup either scheduled or cpu based auto scaling in AWS. 'Scheduled Scaling' allows you to auto scale based on time. You can scale up the application at one time and scale it back down at another time. This will allow you to run jobs at certain times and also turn down applications at night if not needed to save on AWS costs. 'CPU Scaling' allows you to auto scale based on CPU utilization. This will setup a Cloudwatch alarm for high and low cpu usage and scale up or down if that threshold is crossed for a specified amount of polling cycles."
                },
                "DownMaxSize": {
                    "title" : "Scaling Down Max Size.",
                    "type": "string",
                    "pattern": "^[0-9]{1,3}$",
                    "description": "Any integer value. This is the maximum number of EC2 instances you want running."
                },
                "DownMinSize": {
                    "title" : "Scaling Down Min Size",
                    "type": "string",
                    "pattern": "^[0-9]{1,3}$",
                    "description" : "Any integer value. This is the minimum number of EC2 instances you want running."
                },
                "DownRecurrence": {
                    "title" : "Scaling Down Recurrence",
                    "type": "string",
                    "description": "The time in UTC time. The format is similar to CRON. This will be the time your application scales down. Example: <0 14 * * *>"
                },
                "UpMaxSize": {
                    "title" : "Scaling Up Max Size",
                    "type": "string",
                    "pattern": "^[0-9]{1,3}$",
                    "description" : "Any integer value. This is the maximum number of EC2 instances you want running."
                },
                "UpMinSize": {
                    "title" : "Scaling Up Min Size",
                    "type": "string",
                    "pattern": "^[0-9]{1,3}$",
                    "description" : "Any integer value. This is the minimum number of EC2 instances you want running."
                },
                "UpRecurrence": {
                    "title" : "Scaling Up Recurrence",
                    "type": "string",
                    "description" : "The time in UTC time. The format is similar to CRON. This will be the time your application scales up. Example: <0 7 * * *>"
                },
                "CpuUp": {
                    "title" : "Cpu utilization upper threshold",
                    "type": "string",
                    "pattern": "^[0-9]{1,10}$",
                    "description": "Any integer value. This is the percent value of CPU utilization you want to use for the high usage threshold. Typically should be set to fairly high value ie: 80 - 99, but may vary based on typical application loads."
                },
                "CpuDown": {
                    "title" : "Cpu utilization lower threshold",
                    "type": "string",
                    "pattern": "^[0-9]{1,10}$",
                    "description": "Any integer value. This is the percent value of CPU utilization you want to use for the low usage threshold alarm that triggers the scale down. Typically should be set to low value ie: 20 - 40, but may vary based on typical application loads."
                },
                "CpuMonitorUpPeriods": {
                    "title" : "Number of polling periods for the High CPU alarm to trigger",
                    "type": "string",
                    "pattern": "^[0-9]{1,10}$",
                    "description": "Used in conjunction with CpuMonitorUpSecs to determine how long of a time period of high CPU utilization to wait before scaling up an instance."
                },
                "CpuMonitorDownPeriods": {
                    "title" : "Number of polling periods for the Low CPU alarm to trigger",
                    "type": "string",
                    "pattern": "^[0-9]{1,10}$",
                    "description": "Used in conjunction with CpuMonitorDownSecs to determine how long of a time period of low CPU utilization to wait before scaling up an instance."
                },
                "CpuMonitorUpSecs": {
                    "type": "string",
                    "pattern": "^[0-9]{1,10}$",
                    "description": "The time over which the average CPU utilization is calculated. You must specify a time in seconds that is also a multiple of 60. Used in conjunction with CpuMonitorUpPeriods to determine how long of a time period of high CPU utilization to wait before triggering the High CPU alarm and scaling up an instance."
                },
                "CpuMonitorDownSecs": {
                    "type": "string",
                    "pattern": "^[0-9]{1,10}$",
                    "description": "The time over which the average CPU utilization is calculated. You must specify a time in seconds that is also a multiple of 60. Used in conjunction with CpuMonitorDownPeriods to determine how long of a time period of low CPU utilization to wait before triggering the Low CPU alarm and scaling down an instance."
                }
            }
        }
    },
    "patternProperties": {
        ".*::custom_jdk$": {
            "enum": ["oraclejdk8", "zulu-8", "zulu-9", "zulu-10"],
            "description" : "[Platform] Optional for dropwizard, tomcat, and springboot - zulu-8, oraclejdk8, zulu-9, zulu-10"
        },
        ".*::app_deploy_file_ext$": {
            "enum": ["war", "jar"],
            "description": "[Platform] Required for tomcat & springboot platforms. Defines the extension of the application artifact being deployed. "
        },
        ".*::app_deploy_name$": {
            "type": "string",
            "description" : "[Platform] Optional for dropwizard, tomcat & springboot. The value is inherited from the {AppName} value provided in the app parameters file. If provided, it will use that name instead of {AppName} to get the artifact, created the application directory, and start the application."
        },
        ".*::app_version$": {
            "type": "string",
            "description" : "[Platform] Set from the --version argument used when calling createStack.py. This value has always been dynamically set by the createStack script."
        },
        ".*::conf_env$": {
            "enum": ["dev", "int", "qa", "prod"],
            "description" : "[Platform] Inherits the value from {TagEnv}."
        },
        ".*::extra_startup_params$": {
            "type": "string",
            "description" : "[Platform] Optional for tomcat and springboot platforms. For use to pass parameters to the java command after the jar filename to start the application. It should be a string as if typed on the command line. Example: -Dspring.profiles.active=default --logging.file=/opt/snimam/logs/availability.log"
        },
        ".*::pre_jar_params$": {
            "type": "string",
            "description" : "[Platform] Optional for tomcat and springboot platforms. For use to pass parameters to the java command before the jar filename to start the application. It should be a string as if typed on the command line. Example: -javaagent:/opt/snimam/applications/trs-server/lib/newrelic-agent-3.19.2.jar -Dnewrelic.config.file=/opt/snimam/applications/trs-server/conf/newrelic.yml"
        },
        ".*::prefix_url$": {
            "type": "string",
            "pattern": "^(https://sni4bees.artifactoryonline.com|https://repo.sniglobalmedia.com)/.*",
            "description" : "[Platform] Required for all platforms. The value is the destination of the application artifact's app non-specific location. Since the full path is built by {AppName} and {app_version}, this would be the prefix to the complete url which includes the account domain and artifactory repository path up to the application's name. Example value: https://sni4bees.artifactoryonline.com/sni4bees/public/com/scrippsnetworks/nonlinear/"
        },
        ".*::health_uri$": {
            "type": "string",
            "description" : "[Platform] Extracted from the {Healthcheck} value provided in the app parameters file."
        },
        ".*::service_port$": {
            "type": "string",
            "description" : "[Platform] Extracted form the {Healthcheck} value provided in the app parameters file."
        },
        "^drop_wizard_deploy::run_command$": {
            "type": "string",
            "description" : "[Platform] [Antiquated] backward compatible for dropwizard platform. Please use ^dropwizard_deploy::run_command$ going forward"
        },
        "^dropwizard_deploy::run_command$": {
            "type": "string",
            "description" : "[Platform] Optional for dropwizard platform. Defaults to server but can be adjusted to be client or to specify different configuration file than the one which named via {AppName} value (denoted by <app_name> below). Example: /opt/snimam/applications/<app_name>/bin/<app_name> server /opt/snimam/applications/<app_name>/conf/<app_name>.yml"
        },
        "^jboss[5-6]{1}_deploy::sn_deploy_name$": {
            "type": "string",
            "description" : "[Platform] Optional for Jboss5 & Jboss6. The value is inherited from the {AppName} value provided in the app parameters file. If provided, it will use that name instead of {AppName} to get the artifact, created the application directory, and start the application."
        },
        "^apache_app_deploy::httpd_conf_file$": {
            "type": "string",
            "description" : "[Platform] Required for angular platform. Custom httpd.conf file which will replace the standard file in /etc/httpd/conf on the EC2s."},
        "^apache_app_deploy::packages$": {
            "enum": ["httpd"],
            "description" : "[Platform] For Angular Project this Specifc version of Apache will be installed  httpd (install Apache 2.4)."},
        "^tomcat_deploy::app_deploy_config_name$": {
            "type": "string",
            "description" : "[Platform] Required for tomcat platform. Specifies the name of the configuration name for the application. Typically, the configuration artifacts are stored as zip file separately from the application artifacts."
        },
        "^tomcat_deploy::app_deploy_config_path$": {
            "type": "string",
            "description" : "[Platform] Optional for tomcat platform. Specifies the an alternate path for the configuration file for the application. Typically, the configuration artifacts are stored as zip file separately from the application artifacts. This will default to tomcat_deploy::app_deploy_config_name if not included."
        }
    },
    "required": ["AppName", "DNSName", "Healthcheck", "Platform", "TagBusUnit", "TagEnv", "TagOwner", "TagProject"],
    "additionalProperties": false

}

[^1]: 0-9

[^2]: 0-9

[^3]: 0-1
