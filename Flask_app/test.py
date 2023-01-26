from flask import Flask, render_template, request, redirect, url_for, Response, abort
import os
from flask import jsonify,make_response
import zipfile,json
from io import BytesIO
from werkzeug.datastructures import FileStorage
import warnings
from flask import Flask, flash, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
import time,subprocess
from flask import Flask
warnings.simplefilter("ignore", DeprecationWarning)


app = Flask(__name__)
UPLOAD_FOLDER = 'flask_code/static/uploads/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_PATH = 'flask_code/static'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("index.html")
    
    obj = request.files.get("file")
    req = request.form

    print(obj)  
    print(obj.filename)  
   
    ret_list = obj.filename.rsplit(".", maxsplit=1)
    if len(ret_list) != 2:
                 return "Please upload zip file"
    if ret_list[1] != "json":
                 return "Please upload zip file"
 
    print("Upload path", UPLOAD_PATH)
    file_path = os.path.join(UPLOAD_PATH, "files", obj.filename) # The path where the uploaded file is saved
    print("filepath",file_path)
    obj.save(file_path)
    target_path = os.path.join(UPLOAD_PATH, "files",obj.filename) # The path where the unzipped files are saved {input this if want to save each file which is uploaded [, str(uuid.uuid4()) ]
    print("target_path",target_path)

    with open(target_path, 'r') as json_file:
        data = json_file.read()

    # command = f'python train.py --config {target_path}'
    # print("executing command",command)

    command = 'python train.py --resume_ckpt "sd_v1-5_vae" --data_root "D:\stable_difussion\stable_code\flask_code\static\files\final\test" --max_epochs 50 --data_root "input" --lr_scheduler cosine --project_name myproj --batch_size 6 --sample_steps 200 --lr 3e-6 --ckpt_every_n_minutes 10 --useadam8bit --ed1_mode'
    print("executing command",command)

    output = subprocess.run(command, shell=True, capture_output=True)
    print(output.stdout.decode())

    print("subprocess running")
    return "Model tarining initiated"


@app.route("/upload_zip", methods=["GET", "POST"])
def upload_zip():
    if request.method == "GET":
        return render_template("index.html")
    
    obj = request.files.get("file")
    req = request.form
    fileid = req.get('fileid')

    ret_list = obj.filename.rsplit(".", maxsplit=1)
    if len(ret_list) != 2:
                 return "Please upload zip file"
    if ret_list[1] != "zip":
                 return "Please upload zip file"
 
    print("Upload path", UPLOAD_PATH)
    file_path = os.path.join(UPLOAD_PATH, "files", obj.filename) # The path where the uploaded file is saved
    print("filepath",file_path)
    obj.save(file_path)
    target_path = os.path.join(UPLOAD_PATH, "files",str(fileid)) # The path where the unzipped files are saved {input this if want to save each file which is uploaded [, str(uuid.uuid4()) ]
    print("target_path",target_path)

    zip_upload(file_path,target_path,fileid)

    return target_path


def unzip_file(zip_src, dst_dir):
    # """
    # Unzip the zip file
    #      :param zip_src: full path of zip file
    #      :param dst_dir: the destination folder to extract to
    # :return:
    # """
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, "r")
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
         return "Please upload zip file"


def zip_upload(file_path,target_path,fileid):
    print("return",file_path,target_path,fileid)
    ret = unzip_file(file_path, target_path)
    os.remove(file_path) # delete file
    data_upload = "data uploded"
    print("File path:",data_upload)
    if ret:
        return ret
    
    return make_response(jsonify(data_upload), 200)  


if __name__ == "__main__":
    app.run(host='0.0.0.0')
