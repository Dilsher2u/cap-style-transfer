#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 07:39:41 2020

@author: dilsher
"""
import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response
from werkzeug.utils import secure_filename
from main import style_image


UPLOAD_FOLDER = os.getcwd()+'/raw'
print(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

filename= ''
bgfile = ''
stylefile = ''
#messages = False
dfile = ''
#dfile = os.path.join(app.config['UPLOAD_FOLDER'], dfile)
class Files():
    def __init__(self):
        self.filename = None
        self.bgfile=None
        self.stylefile=None
        self.dfile = None
    
    def get_filename(self):
        return self.filename
    
    def get_bgfile(self):
        return self.bgfile
    
    def get_stylefile(self):
        return self.stylefile
    
    def get_dfile(self):
        return self.dfile
    
    def set_filename(self, filename):
        self.filename = filename
    
    def set_bgfile(self, bgfile):
        self.bgfile = bgfile
    
    def set_stylefile(self, stylefile):
        self.stylefile = stylefile
        
    def set_dfile(self, dfile):
        self.dfile = dfile

files_upload = Files()
        
        
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/download', methods=['GET', 'POST'])
def download_Image(): 
    global files_upload
    print('in download - '+files_upload.dfile)
            
    return render_template('download.html', dfile=files_upload.get_dfile())



@app.route('/style', methods=['GET', 'POST'])
def choose_StyleImage():
    
    global files_upload
    if request.method == 'POST':
        print(UPLOAD_FOLDER)
        print('in style- - '+files_upload.get_filename())
        print('in style - '+files_upload.get_bgfile())
        files_upload.set_stylefile(request.form['stylefile'])
        print('in style - '+files_upload.get_stylefile())
        img = style_image(UPLOAD_FOLDER,files_upload.get_filename(), files_upload.get_bgfile(), files_upload.get_stylefile())
        print(img)
        #messages = True
        files_upload.set_dfile(img)
     #   print('image type',+type(dfile))
        #img.show()
        
        #return render_template('download.html', dfile=dfile)
        return redirect(url_for('download_Image'))
    
    return render_template('style_images.html')

        
@app.route('/choose', methods=['GET', 'POST'])
def choose_bgImage():
    global files_upload
    if request.method == 'POST':
        print('in choose - '+files_upload.get_filename())
        files_upload.set_bgfile(request.form['bgfile'])
        print('in choose - '+files_upload.get_bgfile())
        return redirect(url_for('choose_StyleImage'))
       
    return render_template('Select_background.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    global files_upload
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            files_upload.set_filename(file.filename)
            print("in upload", files_upload.get_filename())
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], files_upload.get_filename()))
            print(files_upload.get_filename())
            #choose_bgImage(filename)
            
            
            return redirect(url_for('choose_bgImage'))
        
    return render_template('index.html')


from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == "__main__":
    app.run()