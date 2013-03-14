import webapp2
        
import jinja2
import os

jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
        
class FloorPlans(webapp2.RequestHandler):
    def get(self):
        template = jinja.get_template('templates/floorPlans.html')
        self.response.out.write(template.render({}))  
        
class PreLease(webapp2.RequestHandler):
    def get(self):
        template = jinja.get_template('templates/preLease.html')
        self.response.out.write(template.render({}))        
        
class Home(webapp2.RequestHandler):
    def get(self):
        template = jinja.get_template('templates/home.html')
        self.response.out.write(template.render({}))
        
app = webapp2.WSGIApplication([
    ('/floor-plans', FloorPlans),
    ('/pre-lease', PreLease),
    ('/', Home),    
], debug=True)