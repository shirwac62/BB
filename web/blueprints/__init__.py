from web.blueprints.contact.view import blueprint as contact
from web.blueprints.login.views import blueprint as login
from web.blueprints.register.view import blueprint as register
from web.blueprints.donor.view import blueprint as donor
from web.blueprints.dashboard.views import blueprint as dashboard


blood_list = [register, login, donor, contact, dashboard]
