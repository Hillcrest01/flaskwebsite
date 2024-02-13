from flask import Flask
#we create a function after importing flask from Flask.
def create_app():
    #we initialize the app. 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'w3cyt4df4uvf54ifgh5gb'
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
#we have created a flask application up to this point.