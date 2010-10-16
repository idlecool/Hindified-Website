from google.appengine.api import urlfetch
from google.appengine.api import images
import os, datetime, md5, sha
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import memcache
import Cookie

class MainPage(webapp.RequestHandler):
    def get(self):
        url = "http://www.hindified.com/lib/captcha/"
        #url = "http://127.0.0.1/captcha/"
        userhash = sha.new(str(datetime.datetime.now().microsecond)).hexdigest()[5:9]
        randlist = list(userhash)
        userid = md5.new(str(datetime.datetime.now().microsecond)).hexdigest()[5:11]
        memcache.add(key=userid, value=userhash, time=3600)
        cookie = Cookie.SimpleCookie()
        cookie["userid"] = userid
        cookie["userid"]["expires"] = (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime("%a, %d-%b-%Y %H:%M:%S GMT")
        print cookie.output()
        print 'Pragma: no-cache'
        print 'Cache-Control: no-cache'
        print 'Expires: -1'
        inputimage = urlfetch.fetch(url+'main.png')
        inputimage1 = urlfetch.fetch(url+randlist[0]+'.png')
        inputimage2 = urlfetch.fetch(url+randlist[1]+'.png')
        inputimage3 = urlfetch.fetch(url+randlist[2]+'.png')
        inputimage4 = urlfetch.fetch(url+randlist[3]+'.png')
        img0 = inputimage.content
        img1 = inputimage1.content
        img2 = inputimage2.content
        img3 = inputimage3.content
        img4 = inputimage4.content
        if inputimage.status_code == 200:
            img5 = images.composite([(img0,0,0,1.0,images.TOP_LEFT),(img1,105,12,1.0,images.TOP_LEFT),(img2,125,12,1.0,images.TOP_LEFT),(img3,145,12,1.0,images.TOP_LEFT),(img4,165,12,1.0,images.TOP_LEFT)],187,45,1,output_encoding=images.PNG,)
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(img5) 

application = webapp.WSGIApplication([('/exim', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
