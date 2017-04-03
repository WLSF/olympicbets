# Django project settings loader
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# You can key the configurations off of anything - I use project path.
configs = {
    '/Users/wlsf/Desktop/wlsf_projects/studies/django/olympicbets/olympicbets': 'settings_development',
    'server': 'settings_production'
}

# Import the configuration settings file - REPLACE projectname with your project

if configs[ROOT_PATH]:
    cfg = configs[ROOT_PATH]
else:
    cfg = configs['server']

config_module = __import__('olympicbets.%s' % cfg, globals(), locals(), 'olympicbets')

# Load the config settings properties into the local scope.
for setting in dir(config_module):
    if setting == setting.upper():
        locals()[setting] = getattr(config_module, setting)