from flask import Flask
from App.apis import init_api



def create_app(env):
    app = Flask(__name__)
    # 初始化API
    init_api(app)

    return app