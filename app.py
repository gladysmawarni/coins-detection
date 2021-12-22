import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from detect import run
from PIL import Image
import pyttsx3

app = Flask(__name__)

weight = r'D:\IronHack\final project\yolov5\runs\train\exp\weights\best.pt'
UPLOAD_FOLDER = r'D:\IronHack\final project\yolov5\static\uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_img(img_path):
	run(weights= weight ,source= img_path, imgsz= [416, 416], conf_thres=0.05, project= 'static/detect', exist_ok= True, save_txt=True, agnostic_nms=True)

def count_coins(name):
    coins_dict ={
        '0': 1,
        '1': 10,
        '2': 100,
        '3': 2,
        '4': 20,
        '5': 200,
        '6': 5,
        '7': 50
    }
    result =[]
    convert = []
    coins_sum = 0 
    total_coints = {}

    path = 'static/detect/exp/labels/'

    doc = open(path + name +'.txt', 'r')
    label = doc.read()
    li = label.split('\n')
    
    for line in li[:-1]:
        result.append(line.split(' ')[0])

    for value in result:
        true = coins_dict[value]
        convert.append(true)
    
    for value in convert:
        coins_sum += value
        if value not in total_coints:
            total_coints[value] = 1
        else:
            total_coints[value] += 1
	
    for i in total_coints:
        return(coins_sum/100)

def text_to_speech(text):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict['Female']

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index1.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            coins = 0
            filename = secure_filename(file.filename)
            image = Image.open(file)
            image.thumbnail([416,416])
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_path
            process_img(img_path)
            
            txt_name = filename[:-4]
            coins = count_coins(txt_name)
            text = 'you have '+ str(coins) + ' euros'
            text_to_speech(text)

    return render_template("index1.html", image = filename, coins=text)



if __name__ =='__main__':
	app.run()