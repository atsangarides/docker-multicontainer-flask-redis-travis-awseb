import os

from app import create_app

app = create_app(os.environ.get('CONFIG'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG'), threaded=True)
