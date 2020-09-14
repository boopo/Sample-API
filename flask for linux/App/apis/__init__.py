from flask_restful import Api
from App.apis.user_api import Dianfeis
api = Api()
def init_api(app):
    api.init_app(app)

api.add_resource(Dianfeis,'/dianfei')


