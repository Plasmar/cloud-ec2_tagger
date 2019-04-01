import boto3
import json

# Across all accounts, these keys and values will be constant and required
required_keys = ["t_environment", "t_name", "t_owner_individual", "t_responsible_individuals",
                 "t_awscon", "t_role", "t_AppID", "t_shut", "t_pillar", "t_cmdb", "t_dcl"]

required_values = ["POC", "DELETE ME", "securityengineering@pearson.com",
                   "securityengineering@pearson.com", "ProofofConcept", "CISO Sandbox", "SVC01342", "No", "Foundation", "No", 3]
# We will make a set out of this list to use its difference() method below 
req_set = set(required_keys)

# Full dicts of the required keys and values
constant_tags = [
    {
        "Key": "t_environment",
        "Value": "POC"
    },
    {
        "Key": "t_name",
        "Value": "DELETE ME"
    },
    {
        "Key": "t_owner_individual",
        "Value": "securityengineering@pearson.com"
    },
    {
        "Key": "t_responsible_individuals",
        "Value": "securityengineering@pearson.com"
    },
    {
        "Key": "t_awscon",
        "Value": "ProofofConcept"
    },
    {
        "Key": "t_role",
        "Value": "CISO Sandbox"
    },
    {
        "Key": "t_AppID",
        "Value": "SVC01342"
    },
    {
        "Key": "t_shut",
        "Value": "No"
    },
    {
        "Key": "t_pillar",
        "Value": "Foundation"
    },
    {
        "Key": "t_cmdb",
        "Value": "No"
    },
    {
        "Key": "t_dcl",
        "Value": 3
    }
]

####################################################################################
# The action begins here...

# Make the connection via boto3
ec2 = boto3.resource('ec2')
ins = ec2.Instance('i-03d6707f5c9b0e3dd')

# Two lists we will use later a few lines down
current_keys = []
not_needed = []

# Just testing this out on one instance at a time
tags = ins.tags
# print(json.dumps(tags, indent=4))
# Need to calculate the following in order to determine which tags needed
for t in tags:
    current_keys.append(t['Key'])

# Create a list of required tags that already exist
for c in constant_tags:
    if c['Key'] in current_keys:
        not_needed.append(c['Key'])

current_set = set(current_keys)
not_needed_set = set(not_needed)

# All required tags, less the ones that we already found when iterating through
needed = req_set.difference(not_needed_set)
print(needed)

length_of_original_required = len(constant_tags)
for i in range(length_of_original_required):
    print(constant_tags[i])
    if constant_tags[i]['Key'] in needed:
        print("create one of thess")

