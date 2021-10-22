from xmlrpc import client

url = 'https://maria-conectsen-online-technical-training4-14-0-dev--3460027.dev.odoo.com/'
db = 'maria-conectsen-online-technical-training4-14-0-dev--3460027'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
common.version()
