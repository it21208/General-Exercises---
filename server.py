"""
Main module of the server file
"""

import os

# 3rd party moudles
from flask import Flask, render_template, redirect, flash, url_for
from flask_bootstrap import Bootstrap
from flask_compress import Compress
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed
from flask_uploads import configure_uploads, IMAGES, UploadSet

from keras.models import load_model
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from gevent.pywsgi import WSGIServer
import matplotlib.pyplot as plt

# http://localhost:8000/

# init app
app = Flask(__name__)
Bootstrap(app)
compress = Compress()
compress.init_app(app)
app.secret_key = "Kvdik0$Loyk3t0"
app.config["UPLOADED_IMAGES_DEST"] = "static/img/uploads"
# init image uploader
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

# Model saved with Keras model.save()
MODEL_PATH = 'models/best_model_val.h5' # C:/Users/dimit/Documents/GitHubs/keras-flask-deploy-webapp

# Load your own trained model
model = load_model(MODEL_PATH)
print('Model loaded. Start serving...')

# upload form

class MyForm(FlaskForm):
    image = FileField('image', validators=[FileAllowed(images, 'Μόνο εικόνες!'), FileRequired('Επιλέξτε αρχείο!')])
    submit = SubmitField('Υπολογισμός')


# Create a URL routes
@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def home():
    form = MyForm()
    if form.validate_on_submit():
        try:
            filename = images.save(form.image.data)
            return redirect(url_for('predict', filename=filename))

        except Exception as e:
            flash('Παρουσιαστηκε καποιο προβλημα κατα το ανεβασμα της φωτογραφιας')

    return render_template("home.html", form=form)


@app.route('/predict/<filename>', methods=['GET'])
def predict(filename):
    image = load_img('static/img/uploads/'+filename, target_size=(400,400,3))
    image = img_to_array(image)
    image /= 255.0
    image = np.expand_dims(image, axis=0)
    #image = preprocess_input(image, mode='tf')
    yhat = model.predict(image)  
    print(yhat)
    age_groups = ["Age-0", "Age-1", "Age-2", "Age-3", "Age-4", "Age-5+"]
    #label = np.argmax(yhat)
    #labelName = age_groups[label]
    #print("Label name:", labelName)
    yhat = 100*yhat
    plt.barh(age_groups,yhat.flatten())
    plt.title('Prediction %)')
    outfile = 'age_pred.png'
    plt.savefig(outfile, dpi = 300)
    return render_template('predict.html', filename=filename, yhat = yhat)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
