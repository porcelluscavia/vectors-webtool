import sys
sys.path.insert(0, '/var/www/html/sfb833/snaut/snaut-master')


from configparser import ConfigParser

from .snaut import app_factory



conf = ConfigParser()

conf.read(['config.ini', 'config_local.ini'])

application = app_factory(conf)