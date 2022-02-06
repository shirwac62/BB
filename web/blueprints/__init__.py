from web.blueprints.login.views import blueprint as login
from web.blueprints.register.view import blueprint as register
from web.blueprints.donor.view import blueprint as donor

blood_list = [register, login, donor]
