
##################################################################
##                                                              ##
##  Name        :       tag_audit.py                            ##
##  Date        :       03.28.2019                              ##
##  Author:     :       Cameron M Merrick                       ##
##  Description :       Parses CSV file to fix missing AWS tags ##
##                                                              ##
##################################################################


import csv
import os
import json
import boto3

# Ensure script ran from the correct directory
available_files = os.listdir()
if "Missing_Tags_data.csv" not in available_files:
    raise FileNotFoundError("You probably ran this from the wrong dir!")

# all of the required tags per the tagging standard document
required_keys = ["t_environment", "t_name", "t_owner_individual", "t_responsible_individuals", "t_awscon", "t_role", "t_AppID", "t_shut", "t_pillar", "t_cmdb", "t_dcl"]
required_set = set(required_keys)

# connect to AWS and load the instances into a 'servers' object
ec2 = boto3.resource('ec2')
# servers = ec2.instance.all()
instance = ec2.Instance('i-03d6707f5c9b0e3dd')

# the tags we want to add.  These are constant across each instance
constant_tags = [
    {
        "Key": "t_environment",
        "Value": "POC"
    },
    {
        "Key": "t_name",
        "Value": "DELETE ME"
    }
    {
        "Key": "t_owner_individual",
        "Value": "securityengineering@pearson.com"
    }
    {
        "Key": "t_responsible_individuals",
        "Value": "securityengineering@pearson.com"
    }
    {
        "Key": "t_awscon",
        "Value": "ProofofConcept"
    }
    {
        "Key": "t_role",
        "Value": "CISO Sandbox"
    }
    {
        "Key": "t_AppID",
        "Value": "SVC01342"
    }
    {
        "Key": "t_shut",
        "Value": "No"
    }
    {
        "Key": "t_pillar",
        "Value": "Foundation"
    }
    {
        "Key": "t_cmdb",
        "Value": "No"
    }
    {
        "Key": "t_dcl",
        "Value": 3
    }
]
"""
for instance in servers:
    instance_tags = instance.tags
    print("######################################")
    print(instance)
    print("######################################")
    print(json.dumps(instance_tags, indent=4))  # pretty print without using pp module
"""
    # temptags = []   # used to hold tag keys for comparison to required tags
    # for tag in instance_tags:
    #     temptags.append(tag['Key'])
    # provided_set = set(temptags)
    # needed_tags = required_set.difference(provided_set)
    # print("\nThe following are tags that need to be created to be compliant:")
    # print(needed_tags)
instance_tags = instance.tags
    for tag in instance_tags:

        for k, v in tag.items():
            # The data structures we will use to hold values before being created in AWS
            sometags = {}                                             
            temp_tag_to_add = []

            # given each instance, and every 
            if not k or if k == 't_environment' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = 'POC'
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_cost_center' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = 10.365.74172.40701.0000.35
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_owner_individual' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "securityengineering@pearson.com"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_responsible_individuals' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "securityengineering@pearson.com"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_awscon' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "ProofofConcept"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_role' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "CISO Sandbox"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_AppID' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "SVC01342"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_shut' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "No"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_pillar' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "Foundation"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_cmdb' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = "No"
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_dcl' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = 3
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)
            if not k or if k == 't_name' and v == 'NEEDED':
                sometags['Key'] = k
                sometags['Value'] = 'DELETE ME'
                temp_tag_to_add.append(sometags)
                instance.create_tags(instance.tags, Tags=temp_tag_to_add)

        # sometags = {}
        # temp_tag_to_add = []
        # sometags['Key'] = t
        # if t == "t_cost_center":
        #     sometags['Value'] = 10.365.74172.40701.0000.35
        # elif t == "t_owner_individual" or t == "t_responsible_individuals":
        #     sometags['Value'] = "securityengineering@pearson.com"
        # elif t == "t_environment":
        #     sometags['Value'] = "POC"
        # elif t == "t_awscon":
        #     sometags['Value'] = "ProofofConcept"
        # elif t == "t_role":
        #     sometags['Value'] = "CISO Sandbox"
        # elif t == "t_AppID":
        #     sometags['Value'] = "SVC01342"
        # elif t == "t_shut":
        #     sometags['Value'] = "No"
        # elif t == "t_pillar":
        #     sometags['Value'] = "Foundation"
        # elif t == "t_cmdb":
        #     sometags['Value'] = "No"
        # elif t == "t_dcl":
        #     sometags['Value'] = 3
        # elif t == "t_name":
        #     sometags['Value'] = "DELETE ME"
        
        # sometags['Value'] = "NEEDED"
        # temp_tag_to_add.append(sometags)
        # instance.create_tags(instance.tags, Tags=temp_tag_to_add)

    print('\n\n\n\n\n')  # spacing to break apart each instance's tag groups


# t_cost_center = 10.365.74172.40701.0000.35
# t_name = "DELETE ME"
# t_owner_individual = "securityengineering@pearson.com"
# t_responsible_individuals = "securityengineering@pearson.com"
# t_environment = "POC"
# t_awscon = "ProofofConcept"
# t_role = "CISO Sandbox"
# t_AppID = "SVC01342"
# t_shut = "No"
# t_pillar = "Foundation"
# t_cmdb = "No"
# t_dcl = 3



    
