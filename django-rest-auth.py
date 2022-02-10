import django
#from documentation, if no user authenticates, 
#request.user returns django.contrib.auth.models.AnonymousUser
#while request.auth returns None

#AUTHENTICATION SCHEME:
#IN SETTINGS.PY --- This is if you want to deny access to all views for non auth users

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

#TO ALLOW ONLY FOR SPECIFIC FUNCTIONS/CLASSES
#Can also be set per view in Class-based views using APIView
#or decorators for function-based views
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([isAuthenticated])
def example_view(request, format=None):
    content = {
        'user':str(request.user),
        'auth':str(request.auth),
    }
    return Response(content);

#remember @api_view decorator must be above all others

ERROR_CODES = {
    '401':'Unauthorized',       #if returning this code, must include WWW-Authenticate Header to tell user how to authenticate
    '403':'Permission Denied'
}

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    nn 
#USING JSONWEBTOKENS

$pip install djangorestframework-jwt

#IN SETTINGS.PY
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated'
    ]
}

#IN URLS.PY, add url link to Obtain token via username and password
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    #...
    url(r'^api-token-auth/', obtain_jwt_token),
    
]

#In order to access protected urls you must include the Header
Authorization: JWT <your-token>
or 
Authorization: Bearer <your token>

#REFRESH TOKEN
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns=[
    #...
    url(r'^api-token-refresh/',refresh_jwt_token),
]
#then pass in the existing tiken to the refresh endpoint as: 
{'token':EXISTING_TOKEN}
#the response shall be similar to the obtain token endpoint
{'token':NEW_TOKEN}


#TO VERIFY EXISTING TOKEN
from rest_framework_jwt.views import verify_jwt_token


urlpatterns=[
    #...
    url(r'^api-token-verify/',verify_jwt_token),
]
#passing a token to endpoint returns 200 response and the token if valid; and 400 Bad request and an error if token invalid

