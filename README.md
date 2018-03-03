# django-rest-slack

A simple REST API for handling and storing Slack events and slash commands.

## Requirements

- Python 3.6
- PostgreSQL
- Django 2.0+

## Running with Zappa

- pip install -r zappa.txt
- `zappa init`
- Create a Postgres DB in AWS RDS
- Update your zappa_settings.json with the `vpc_config` information:
`
    "vpc_config" : {
        "SubnetIds": [ "subnet-<id>","subnet-<id>" ],
        "SecurityGroupIds": [ "sg-<id>" ]
    }
`
- `zappa deploy <stage>`
- Add the AWS address to your `ALLOWED_HOSTS`
- `zappa update <stage>`

That's basically it.

## Creating a superuser

echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | zappa invoke production --raw 


## Todo

- More detailed instructions / examples
- Refactor model
