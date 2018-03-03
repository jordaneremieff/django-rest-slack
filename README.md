# django-rest-slack

A simple REST API for handling and storing Slack events and slash commands.

## Requirements

- Python 3.6
- PostgreSQL
- Django 2.0+

# Running with Zappa

- pip install -r zappa.txt
- zappa init
- Create a Postgres DB in AWS RDS
- Update your zappa_settings.json with the `vpc_config` information:
`
    "vpc_config" : {
        "SubnetIds": [ "subnet-<id>","subnet-<id>" ],
        "SecurityGroupIds": [ "sg-<id>" ]
    }
`
- 