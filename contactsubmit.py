import os, Cookie
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import memcache
from google.appengine.api import mail

class ContactSubmit(webapp.RequestHandler):
    def post(self):
        try:
            cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        except (Cookie.CookieError, KeyError):
            cookie = False

        if (cookie):
            userhash = memcache.get(cookie['userid'].value)
        else:
            userhash = False

        clientname = self.request.get('name')
        clientemail = self.request.get('email')
        clientorganisation = self.request.get('organisation')
        clientdescription = self.request.get('description')
        clientcaptcha = self.request.get('captcha_input')

        memcache.delete(cookie['userid'].value)

        senderemail = clientname+" <"+clientemail+">"
        emailbody = clientname+"\n"+senderemail+"\n"+clientorganisation+"\n"+clientdescription

        if (userhash):
            if(userhash == clientcaptcha):
                mail.send_mail('idlecool@hindified.com', 'Shiv Deepak <idlecool@gmail.com>', 'Client Query: Hindified Design Studio', emailbody)
                template_values = {
                    'home_url': '/',
                    'home_button_url': 'images/button.png',
                    'back_url': '/contact',
                    'back_button_url': 'images/back_but_act.png',
                    'next_url': '/contact',
                    'next_button_url': 'images/end_but.png',
                    'submit_button_url': 'images/submit_but.png',
                    'home_banner_link': 'images/banner.png',
                    'clientname': clientname,
                    'contactpage': True,
                    }

                path = os.path.join(os.path.dirname(__file__), 'template/contactsubmit.html')
                self.response.out.write(template.render(path, template_values))

            else:
                self.redirect("/contact?captcha=invalid")
        else:
            self.redirect("/contact?captcha=invalid")

application = webapp.WSGIApplication([('/contactsubmit', ContactSubmit)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
