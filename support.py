import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Support(webapp.RequestHandler):
    def get(self):
        template_values = {
            'home_url': '/',
            'home_button_url': 'images/button.png',
            'back_url': '/services',
            'back_button_url': 'images/back_but_act.png',
            'next_url': '/contact',
            'next_button_url': 'images/next_but_act.png',
            'support_image_url': 'images/support.png',
            'supportpage': True,
            }

        path = os.path.join(os.path.dirname(__file__), 'template/support.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/support', Support)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
