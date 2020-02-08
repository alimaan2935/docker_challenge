from flask import Flask, render_template, request
# from flask_uploads import UploadSet, configure_uploads,IMAGES
from PIL import Image

#for regular expressions, saves time dealing with string data
import re
#system level operations (like loading files)
import sys
#for reading operating system data
import os
#tell our app where our saved model is
sys.path.append(os.path.abspath("./model"))
from predict import predict_image
#initalize our flask app
app = Flask(__name__)


# photos = UploadSet('photos', IMAGES)

# app.config['UPLOADED_PHOTOS_DEST'] = '.'
# configure_uploads(app, photos)

@app.route('/')
def index():
	#initModel()
	#render out pre-built HTML file right on the index page
	return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST' and 'photo' in request.files:
		# filename = photos.save(request.files['photo'])
		img = Image.open(request.files['photo'].stream)
		# os.rename('./'+filename,'./'+'output.png')

	print("debug")
	#read the image into memory
	# img = Image.open('./output.png')
	results = predict_image(img)

	print(results)

	# return render_template("index2.html",s1 = s1, s2 = s2, s3 = s3,s4 = s4,s5 = s5,s6 = s6)
	return render_template("index2.html", results=results)


if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port, ssl_context='adhoc')
	#optional if we want to run in debugging mode
	#app.run(debug=True)
