from xmlrpc import client

url = 'https://maria-conectsen-online-technical-training4-14-0-dev--3460027.dev.odoo.com/'
db = 'maria-conectsen-online-technical-training4-14-0-dev--3460027'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db,uid, password,
                                'sale.order', 'check_access_rights',
                                ['write'],{'raise_exception':False})
print(model_access)
