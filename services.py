import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Services(webapp.RequestHandler):
    def get(self):
        template_values = {
            'home_url': '/',
            'home_button_url': 'images/button.png',
            'back_url': '/',
            'back_button_url': 'images/back_but_act.png',
            'next_url': '/support',
            'next_button_url': 'images/next_but_act.png',
            'submit_button_url': 'images/submit_but.png',
            'services_image_url': 'images/services.png',
            'servicespage': True,
            }

        path = os.path.join(os.path.dirname(__file__), 'template/services.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/services', Services)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
