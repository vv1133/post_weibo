#! /usr/bin/python

from weibo import APIClient
from re import split
import urllib,httplib
import sys

APP_KEY = '679748153' #youre app key
APP_SECRET = 'fdcabb93a8b53508879654ddff9e07aa' #youre app secret 
# callback url, your must set this URL in your "my application->appInfos-> advanced  info"
CALLBACK_URL = 'http://vdisk.weibo.com/s/dcRgSkvjaW9o'
ACCOUNT = 'xxxx@sina.com'#your email address
PASSWORD = 'xxxxx'     #your pw

#for getting the code contained in the callback url
def get_code(url):
    conn = httplib.HTTPSConnection('api.weibo.com')
    postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','userId':ACCOUNT,'passwd':PASSWORD,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
    conn.request('POST','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'})
    res = conn.getresponse()
    location = res.getheader('location')
    code = location.split('=')[1]
    conn.close()
    return code

def post_weibo(post_contents):
    print "weibo posting..."
    #for getting the authorize url
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    code = get_code(url)
    r = client.request_access_token(code)
    access_token = r.access_token # The token return by sina
    expires_in = r.expires_in
    #save the access token
    client.set_access_token(access_token, expires_in)
    results = client.post.statuses__update(status=post_contents)
    return results

post_weibo(sys.argv[1])

