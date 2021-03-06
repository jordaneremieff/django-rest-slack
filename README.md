# django-rest-slack

A simple, reusable Django app for handling and storing Slack events and slash commands.

## Requirements

- Python 3.6
- PostgreSQL
- Django 2.0+
- DRF

## Setup

- `pip install django django-rest-framework django-rest-slack psycopg2-binary`

- Include the following to your settings.py:

``` 
    INSTALLED_APPS = [
        'rest_framework',
        'rest_slack',
    ]
```

- Include the following to your urls.py:

```
    from django.conf.urls import include
    from rest_slack.views import DRSEventView, DRSCommandView


    api_patterns = ([
            path('events/', DRSEventView.as_view()),
            path('commands/', DRSCommandView.as_view()),
         ], 'api')


    urlpatterns += [
        path('api/v1/', include(api_patterns)),
    ]
```

- Add your environment variables:

```
    export SLACK_CLIENT_ID='your-credential'
    export SLACK_CLIENT_SECRET='your-credential'
    export SLACK_VERIFICATION_TOKEN='your-credential'
    export SLACK_BOT_USER_TOKEN='your-credential'
```

## Running with Zappa

- `pip install zappa`

- `zappa init`

- Create a Postgres DB in AWS RDS

- Update your zappa_settings.json with the `vpc_config` information:
```
    "vpc_config" : {
        "SubnetIds": [ "subnet-<id>","subnet-<id>" ],
        "SecurityGroupIds": [ "sg-<id>" ]
    }
```

- `zappa deploy <stage>`

- Update your settings.py with the hostname created in AWS
```    
    ALLOWED_HOSTS = ['host.name']
```

- `zappa update <stage>`

## Todo

- More detailed instructions / examples
