import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Contact(webapp.RequestHandler):
    def get(self):
        if(self.request.get('captcha')=='invalid'):
            invalidcaptcha = True
        else:
            invalidcaptcha = False

        template_values = {
            'home_url': '/',
            'home_button_url': 'images/button.png',
            'back_url': '/support',
            'back_button_url': 'images/back_but_act.png',
            'next_url': '',
            'next_button_url': 'images/refresh_captcha.png',
            'submit_button_url': 'images/submit_but.png',
            'invalidcaptcha': invalidcaptcha,
            'contactpage': True,
            }

        path = os.path.join(os.path.dirname(__file__), 'template/contact.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/contact', Contact)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
