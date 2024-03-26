from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def do_get():
    return f'Александр Волжанин {datetime.now().strftime('%d.%m.%y %H:%M:%S')}'

if __name__ == '__main__':
    app.run('127.0.0.1',8080) # aka serve_forever()
