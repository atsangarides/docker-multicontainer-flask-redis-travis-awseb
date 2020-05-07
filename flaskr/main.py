import os

from config import config
from app import create_app

app = create_app(config[os.environ.get('ENV')])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG'), threaded=True)
