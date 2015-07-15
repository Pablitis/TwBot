import webapp2
from google.appengine.api import mail

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, Dan Abadie! <3')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
