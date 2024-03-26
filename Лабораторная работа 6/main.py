from flask import Flask, send_file, request
from PIL import Image
from json import dumps


app = Flask(__name__)

@app.route('/')
def get_on_the_page_image():
    try:
        width, height = Image.open("Снимок экрана 2024-03-19 в 23.31.44.png").size
        return dumps({"width": width, "height": height})
    except:
        return dumps({"result":"invalid filetype"})
    
@app.route('/login')
def get_login():
    login_moodle = "1141531"
    return dumps({"login in moodle": login_moodle})

@app.route('/image')
def get_image_size():
    try:
        image_path = 'Снимок экрана 2024-03-19 в 23.31.44.png'
        return send_file(image_path, mimetype='image/jpg')
    except:
        return dumps({"result":"invalid filetype"})

if __name__ == '__main__':
    app.run()
