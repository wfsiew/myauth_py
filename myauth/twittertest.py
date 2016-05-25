import urllib
from hashlib import sha1
import hmac

key = 'iJQGXxO7CsFBIElUhXappxPYv'
secret = 'JdsifIuJ47yUEzCitzpNjcVYO8n6ezS8BEh0456prCiIvZ0EJU'
token_secret = ' gY1W2EZigjn9hucOCpanXG9jJqpOyfr3SACJjgGB9gVwK'

k = urllib.quote('http://localhost:8000/main', safe='')
print k

prm = 'include_entities=true&oauth_consumer_key=xvz1evFS4wEEPTGEFPHBog&oauth_nonce=kYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1318622958&oauth_token=370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb&oauth_version=1.0&status=Hello%20Ladies%20%2B%20Gentlemen%2C%20a%20signed%20OAuth%20request%21'

sig = 'POST&https%3A%2F%2Fapi.twitter.com%2F1%2Fstatuses%2Fupdate.json&include_entities%3Dtrue%26oauth_consumer_key%3Dxvz1evFS4wEEPTGEFPHBog%26oauth_nonce%3DkYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1318622958%26oauth_token%3D370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb%26oauth_version%3D1.0%26status%3DHello%2520Ladies%2520%252B%2520Gentlemen%252C%2520a%2520signed%2520OAuth%2520request%2521'

signkey = 'kAcSOqF21Fu85e7zjz7ZN2U4ZRhfV3WpwPAoE3Z7kBw&LswwdoUaIvS8ltyTt5jkRh4J50vUPVVHtR2YPi5kE'

hashed = hmac.new(signkey, sig, sha1)

j = hashed.digest().encode("base64").rstrip('\n')
print j

import oauth2 as oauth
import urlparse, requests

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key=key, secret=secret)

# Request token URL for Twitter.
request_token_url = "https://api.twitter.com/oauth/request_token"

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")
print resp
print content
h = urlparse.parse_qs(content)
oauth_token = h['oauth_token'][0]
r = requests.get('https://api.twitter.com/oauth/authenticate', params={'oauth_token': oauth_token})
print r.text
