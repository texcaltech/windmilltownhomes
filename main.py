import webapp2
        
import jinja2
import os

jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
        
def getBackground(page):
    bg = {}
    if (page == 'contact'):
        bg['large'] = 'http://farm9.staticflickr.com/8382/8552707810_b5110806a8_h.jpg'
        bg['small'] = 'http://farm9.staticflickr.com/8382/8552707810_e3a58d737f_c.jpg'
    elif (page == 'floorPlans'):
        bg['large'] = 'http://farm9.staticflickr.com/8382/8552707810_b5110806a8_h.jpg'
        bg['small'] = 'http://farm9.staticflickr.com/8382/8552707810_e3a58d737f_c.jpg'
    elif (page == 'home'):
        bg['large'] = 'http://farm9.staticflickr.com/8382/8552707810_b5110806a8_h.jpg'
        bg['small'] = 'http://farm9.staticflickr.com/8382/8552707810_e3a58d737f_c.jpg'
    elif (page == 'location'):
        bg['large'] = 'http://farm9.staticflickr.com/8382/8552707810_b5110806a8_h.jpg'
        bg['small'] = 'http://farm9.staticflickr.com/8382/8552707810_e3a58d737f_c.jpg'
    elif (page == 'preLease'):
        bg['large'] = 'http://farm9.staticflickr.com/8382/8552707810_b5110806a8_h.jpg'
        bg['small'] = 'http://farm9.staticflickr.com/8382/8552707810_e3a58d737f_c.jpg'
    else:
        bg['large'] = 'http://farm9.staticflickr.com/8382/8552707810_b5110806a8_h.jpg'
        bg['small'] = 'http://farm9.staticflickr.com/8382/8552707810_e3a58d737f.jpg'
    return bg
        
class Contact(webapp2.RequestHandler):
    def get(self):
        vars = {}
        vars['bg'] = getBackground('contact')
        template = jinja.get_template('templates/contact.html')
        self.response.out.write(template.render(vars))        
        
class FloorPlans(webapp2.RequestHandler):
    def get(self):
        vars = {}
        vars['bg'] = getBackground('floorPlans')
        template = jinja.get_template('templates/floorPlans.html')
        self.response.out.write(template.render(vars))  
        
class Home(webapp2.RequestHandler):
    def get(self):
        vars = {}
        vars['bg'] = getBackground('home')
        template = jinja.get_template('templates/home.html')
        self.response.out.write(template.render(vars))        
        
class Location(webapp2.RequestHandler):
    def get(self):        
        vars = {}
        vars['bg'] = getBackground('location')
        template = jinja.get_template('templates/location.html')
        self.response.out.write(template.render(vars))
    
class PayRent(webapp2.RequestHandler):
    def get(self):
        vars = {}
        vars['bg'] = getBackground('payRent')
        template = jinja.get_template('templates/payRent.html')
        self.response.out.write(template.render(vars))
        
class PreLease(webapp2.RequestHandler):
    def get(self):
        vars = {}
        vars['bg'] = getBackground('preLease')
        template = jinja.get_template('templates/preLease.html')
        self.response.out.write(template.render(vars))        
        
app = webapp2.WSGIApplication([
    ('/contact', Contact),
    ('/floor-plans', FloorPlans),
    ('/location', Location),
    ('/maintenance', Contact),
    ('/pay-rent', PayRent),
    ('/pre-lease', PreLease),
    ('/', Home),    
], debug=True)