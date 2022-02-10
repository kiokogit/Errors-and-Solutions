#install djongo - the addon to use Mongo with Django
"""pip install djongo"""

#edit db params in settings file

DATABASES={
    'default':{
        'ENGINE': 'djongo',
        'NAME':'my-db-name',
        'CLIENT':{
            'host':'my-db-host'
        }
    }
}

#run command to migrate 
"""python manage.py makemigrations"""
"""python manage.py migrate"""

#There are other alternatives to this - such as pymongo and mongoengine.
#pymongo is best for mongo schemas, while djongo is best with SQL structured data
