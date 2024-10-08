from flask import Flask

from views import views

from pandas import pandas 
app = Flask(__name__)

app.register_blueprint(views, url_prefix="/home")


if __name__ == '__main__':
    app.run(debug=True, port='8081')
