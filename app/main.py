from flask import Flask, render_template, request, session, redirect, url_for
from flask_restful import Api
from controllers.upload import UploadImage
from controllers.search import SearchImage
from models.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/versa-ai-test?ssl_disabled=1'
db.init_app(app)

api = Api(app)
api.add_resource(UploadImage, '/upload')
api.add_resource(SearchImage, '/search')

if __name__ == '__main__':
    app.run(debug=True)