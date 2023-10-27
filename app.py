from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, MultipleFileField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed
from main_cleaning import final_operation
import time
from final_file import final_file_output

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = "static\\files"

class UploadFileForm(FlaskForm):
    files = MultipleFileField('File(s)', validators=[InputRequired(), FileAllowed(['xlsx', 'csv'], 'Excel and CSV files only!')])
    submit = SubmitField("Upload File & Clean")


@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        files_filename = []
        for file in form.files.data:
            files_filename.append(file.filename)
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], file.filename))
        
        result = final_operation(files_filename)
        return render_template('uploaded.html', files_filename=files_filename, result=result)
    
    return render_template('index.html', form=form)


# @app.route('')



if __name__ == "__main__":
    app.run(debug=True)
