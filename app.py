from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = "static\\files"

class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[InputRequired(), FileAllowed(['xlsx', 'csv'], 'Excel and CSV files only!')])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "File has been uploaded"
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
