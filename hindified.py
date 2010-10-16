import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {
            'home_url': '/',
            'home_button_url': 'images/button.png',
            'back_url': '',
            'back_button_url': 'images/end_but.png',
            'next_url': '/services',
            'next_button_url': 'images/next_but_act.png',
            'submit_button_url': 'images/submit_but.png',
            'home_banner_link': 'images/banner.png',
            'homepage': True,
            }

        path = os.path.join(os.path.dirname(__file__), 'template/home.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
