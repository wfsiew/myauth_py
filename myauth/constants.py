from django.conf import settings

class Google(object):
    url = 'http://localhost:8000/google/callback/' if settings.DEBUG else 'https://apps.redtone.com:8585/oauth/google/callback/'

class Facebook(object):
    url = 'http://localhost:8000/facebook/callback/' if settings.DEBUG else 'https://apps.redtone.com:8585/oauth/facebook/callback/'

class Instagram(object):
    url = 'http://localhost:8000/instagram/callback/' if settings.DEBUG else 'https://apps.redtone.com:8585/oauth/instagram/callback/'

class Linkedin(object):
    url = 'http://localhost:8000/linkedin/callback/' if settings.DEBUG else 'https://apps.redtone.com:8585/oauth/linkedin/callback/'

class Live(object):
    url = 'http://localhost:8000/live/callback/' if settings.DEBUG else 'https://apps.redtone.com:8585/oauth/live/callback/'