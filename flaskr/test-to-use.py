import configparser
from flask import Flask
app=Flask(__name__)
cf = configparser.ConfigParser()
cf.read('flaskr.conf')
sec = cf.sections()
print('sections = %s' % sec)
opts = cf.options('USER')
print('opts = %s' % opts)
print(cf['USER']['USERNAME'])
print(Flask.config)