from flask import Flask, request, render_template
import os
import rembg_ai

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods = ['GET','POST'])
def index():
    text = None
    image_path = None
    rembg_path = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            text= 'No file part'

        upload_file = request.files['file']

        if upload_file:
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'], upload_file.filename))
            text= 'File uploaded successfully'
            image_path = upload_file.filename
            rembg_path = rembg_ai.remove_background('static/uploads/'+image_path)

                
    return render_template('index.html',title = 'home',text=text,img_path=image_path,rembg_path =rembg_path)


if __name__ == '__main__':
    app.run(debug=True,port=1234)
