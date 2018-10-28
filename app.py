from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import resources
import tools as t
from api.ini_api import IAPI
from api import dbclasses


app = Flask(__name__)
app.secret_key = t.get_secret_key()
app.register_blueprint(resources.resrc, url_prefix='')


#app.config['DATABASE_FILE'] = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = IAPI.getDBLink()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True, port=5080, host='0.0.0.0')


