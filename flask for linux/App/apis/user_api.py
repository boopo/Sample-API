

from flask import request
from flask_restful import Resource

from App.request import pc


class Dianfeis(Resource):
  def post(self):
    home = request.form.get('home')
    num = request.form.get('num')
    dianfei = pc(home,num)
    return {
            "status":"200",
            "msg":"ok",
            "data":dianfei
    }








