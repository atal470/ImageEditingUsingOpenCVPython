
from flask import Flask, flash, request, redirect, url_for,request,render_template
from werkzeug.utils import secure_filename
import os
print("yehi maar rha error 99")
import cv2
print("yehi maar rha error 1")
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
print("yehi maar rha error 2")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def processimage(filename,operation):

	print(f"The operation is {operation}{filename}")
	print("yehi maar rha error")
	img=cv2.imread(f"static/{filename}")

	if operation == "cgray" :
		imgprocessed=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		newfilename=f"static/{filename}"
		cv2.imwrite(f"static/{filename}", imgprocessed)
		return newfilename
	elif operation == "cpng" :
		newfilename = f"static/{filename.split('.')[0]}.png"
		cv2.imwrite(f"static/{filename.split('.')[0]}.png", img)
		return newfilename
	elif operation == "cjpg" :
		newfilename = f"static/{filename.split('.')[0]}.cjpg"
		cv2.imwrite(newfilename, img)
		return newfilename

	elif operation == "cwebp" :
		newfilename = f"static/{filename.split('.')[0]}.webp"
		cv2.imwrite(f"static/{filename.split('.')[0]}.webp", img)
		return newfilename

	pass

@app.route('/')

def hello_world():

	return render_template("index.html")
@app.route('/about')

def about_html():
	return render_template("about.html")

@app.route('/edit',methods=['GET','POST'])
def edit_html():

	if request.method=='POST':

		operation=request.form.get("operation")
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']

		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			new=processimage(filename,operation)
			flash(f"the file is <a href='/{new}'here>")
			return render_template("index.html")
	return "post"


if __name__ == '__main__':

	app.run(host='0.0.0.0',port=5005,debug=True)

