from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
import requests, uuid, constants, urlparse
import oauth2 as oauth

def index(req):
    google = ('https://accounts.google.com/o/oauth2/auth'
              '?response_type=code'
              '&client_id=579168859503.apps.googleusercontent.com'
              '&redirect_uri={0}'
              '&scope=openid%20profile%20email'
              '&login_hint=email'
              '&approval_prompt=force').format(constants.Google.url)

    fb = ('https://www.facebook.com/dialog/oauth'
          '?response_type=code'
          '&client_id=239282433100666'
          '&redirect_uri={0}'
          '&scope=email').format(constants.Facebook.url)

    instagram = ('https://api.instagram.com/oauth/authorize/'
                 '?client_id=8b86537408774c258d468aa4c3db3207'
                 '&redirect_uri={0}'
                 '&response_type=code').format(constants.Instagram.url)

    linkedin = ('https://www.linkedin.com/uas/oauth2/authorization'
                '?response_type=code'
                '&client_id=756bpc1njs21xy'
                '&redirect_uri={0}'
                '&state={1}').format(constants.Linkedin.url, str(uuid.uuid4()))

    live = ('https://login.live.com/oauth20_authorize.srf'
            '?response_type=code'
            '&client_id=49b7001a-8869-4057-9548-10784e7325f9'
            '&redirect_uri={0}'
            '&scope=wl.basic wl.emails').format(constants.Live.url)
    
    ctx = {
        'google': google,
        'facebook': fb,
        'instagram': instagram,
        'linkedin': linkedin,
        'live': live
    }

    return render(req, 'myauth/index.html', context=ctx)

def twitter_view(req):
    key = 'iJQGXxO7CsFBIElUhXappxPYv'
    secret = 'JdsifIuJ47yUEzCitzpNjcVYO8n6ezS8BEh0456prCiIvZ0EJU'
    consumer = oauth.Consumer(key=key, secret=secret)
    client = oauth.Client(consumer)

    url = 'https://api.twitter.com/oauth/request_token'
    resp, content = client.request(url, "GET")
    m = urlparse.parse_qs(content)
    oauth_token = m['oauth_token'][0]
    k = {
        'oauth_token': oauth_token
    }
    r = requests.get('https://api.twitter.com/oauth/authenticate', params=k)
    return HttpResponse(r.text)

def twitter_callback(req):
    oauth_token = req.GET.get('oauth_token')
    oauth_verifier = req.GET.get('oauth_verifier')
    key = 'iJQGXxO7CsFBIElUhXappxPYv'
    secret = 'JdsifIuJ47yUEzCitzpNjcVYO8n6ezS8BEh0456prCiIvZ0EJU'
    consumer = oauth.Consumer(key=key, secret=secret)
    client = oauth.Client(consumer)

    url = 'https://api.twitter.com/oauth/access_token'
    resp, content = client.request(url, "GET")
    return HttpResponse(content)

def google_callback(req):
    code = req.GET.get('code')
    url = 'https://accounts.google.com/o/oauth2/token'
    k = {
        'code': code,
        'client_id': '579168859503.apps.googleusercontent.com',
        'client_secret': 'G-WYqCt2UGYZRKq3V4o10wli',
        'redirect_uri': constants.Google.url,
        'grant_type': 'authorization_code'
    }
    r = requests.post(url, data=k)
    d = r.json()
    print d
    
    url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    k = {
        'access_token': d.get('access_token')
    }
    r = requests.get(url, params=k)
    m = r.json()
    return JsonResponse(m)

def facebook_callback(req):
    code = req.GET.get('code')
    url = 'https://graph.facebook.com/oauth/access_token'
    k = {
        'code': code,
        'client_id': '239282433100666',
        'client_secret': 'dfee9766ec4e416c528b77f5b3040c48',
        'redirect_uri': constants.Facebook.url,
        'grant_type': 'authorization_code'
    }
    r = requests.post(url, data=k)
    d = r.text
    print d

    l = d.split('&')
    access_token = l[0].replace('access_token=', '')

    url = 'https://graph.facebook.com/me'
    k = {
        'access_token': access_token,
        'fields': 'id,first_name,last_name,email,picture'
    }
    r = requests.get(url, params=k)
    m = r.json()
    return JsonResponse(m)

def instagram_callback(req):
    code = req.GET.get('code')
    url = 'https://api.instagram.com/oauth/access_token'
    k = {
        'code': code,
        'client_id': '8b86537408774c258d468aa4c3db3207',
        'client_secret': '676392bc986740c1866b572a043d7a3c',
        'redirect_uri': constants.Instagram.url,
        'grant_type': 'authorization_code'
    }
    r = requests.post(url, data=k)
    m = r.json()
    return JsonResponse(m)

def linkedin_callback(req):
    code = req.GET.get('code')
    url = 'https://www.linkedin.com/uas/oauth2/accessToken'
    k = {
        'code': code,
        'client_id': '756bpc1njs21xy',
        'client_secret': 'jNqljpC3PnLA7wCP',
        'redirect_uri': constants.Linkedin.url,
        'grant_type': 'authorization_code'
    }
    r = requests.post(url, data=k)
    d = r.json()
    print d
    
    url = 'https://api.linkedin.com/v1/people/~:(id,email-address,first-name,last-name,picture-url)'
    h = {
        'Authorization': 'Bearer {0}'.format(d['access_token'])
    }
    r = requests.get(url, headers=h)
    m = r.text
    print m
    return HttpResponse(m, content_type='text/xml')

def live_callback(req):
    code = req.GET.get('code')
    url = 'https://login.live.com/oauth20_token.srf'
    k = {
        'code': code,
        'client_id': '49b7001a-8869-4057-9548-10784e7325f9',
        'client_secret': 'DVrjot8izkPnZmmigTaeKmW',
        'redirect_uri': constants.Live.url,
        'grant_type': 'authorization_code'
    }
    r = requests.post(url, data=k)
    d = r.json()
    print d
    
    url = 'https://apis.live.net/v5.0/me'
    k = {
        'access_token': d.get('access_token')
    }
    r = requests.get(url, params=k)
    m = r.json()
    return JsonResponse(m)