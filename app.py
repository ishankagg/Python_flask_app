from flask import Flask, render_template, url_for, send_from_directory, redirect
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, MultipleFileField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed
import time
import subprocess
import sys

sys.path.insert(0,'scripts')

from main_cleaning import final_operation

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
        # try:
        for file in form.files.data:
            files_filename.append(file.filename)
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], file.filename))
        
        result = final_operation(files_filename)
        return render_template('uploaded.html', files_filename=files_filename, result=result)
        # trying new branch
        # trying new branch
        # except Exception as e:

    
    return render_template('index.html', form=form)

@app.route('/download_final_file', methods=['GET', 'POST'])
def download_final_file():
    # Execute the final_file.py script in the background
    subprocess.Popen(['python', 'scripts/final_file.py'])

    # Specify the directory where the final file should be located
    output_dir = 'output'
    final_file_name = 'files_combined.csv'
    final_file_path = os.path.join(output_dir, final_file_name)

    max_attempts = 10  # Maximum number of attempts to check for the file
    attempt = 0

    while attempt < max_attempts:
        if os.path.exists(final_file_path):
            return send_from_directory(output_dir, final_file_name, as_attachment=True)
        else:
            attempt += 1
            time.sleep(1)  # Wait for 1 second before the next attempt

    # Handle the case where the final file doesn't exist after the maximum number of attempts
    return "The final file could not be found after multiple attempts."


@app.route('/download_dashboard_file', methods=['GET', 'POST'])
def download_dashboard_file():
    # Specify the directory where the final file should be located
    output_dir = 'output'
    final_file_name = 'files_combined.csv'
    final_file_path = os.path.join(output_dir, final_file_name)
    
    # Execute the final_file.py script in the background
    if os.path.exists(final_file_path) == False:    
        process = subprocess.Popen(['python', 'scripts/final_file.py'])
        process.wait()

    # Execute the dashboard_file.py in the background
    subprocess.Popen(['python', 'scripts/dashboard_file.py'])
    
    # Specify the directory where the dashboard file should be located
    dashboard_file_name = 'dashboard_file.xlsx'
    dashboard_file_path = os.path.join(output_dir, dashboard_file_name)

    second_max_attempts = 10  # Maximum number of attempts to check for the file
    second_attempt = 0

    while second_attempt < second_max_attempts:
        if os.path.exists(dashboard_file_path):
            # Execute the final_file.py script in the background
            return send_from_directory(output_dir, dashboard_file_name, as_attachment=True)
        else:
            second_attempt += 1
            time.sleep(1)  # Wait for 1 second before the next attempt

    # Handle the case where the final file doesn't exist after the maximum number of attempts
    return "The Dashboard file could not be found after multiple attempts."


@app.route('/clean_files', methods=['GET', 'POST'])
def clean_files():
    process = subprocess.Popen(['python', 'scripts/clean_files.py'])
    process.wait()

    return redirect("/upload", code=302)



if __name__ == "__main__":
    app.run(debug=True)
