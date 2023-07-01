from flask import Flask, render_template, request
from colorthief import ColorThief
from func import *
from PIL import Image
import io
import base64

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/palette")
def palette():
    return render_template('palette.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'imageUpload' in request.files:
        image = request.files['imageUpload']
        # Perform further processing with the uploaded image here
        img_data = image.read()
        
        img_base64 = base64.b64encode(img_data).decode('utf-8')

        palette=get_palette(image)
        colors=[]
        print(palette)
        for rgb in palette:
            color=rgb_to_html_color(rgb)
            colors.append(color)

            


        # Return the HTML element
        return render_template('palette.html',colors=colors,  image_url=img_base64)
    else:
        return "No file uploaded."

if __name__ == '__main__':
    app.run(debug=True)
