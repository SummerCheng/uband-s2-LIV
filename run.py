from flask import Flask
from flask import render_template
import json
import codecs

app = Flask(__name__)

def readJson(json_name):
	file_text=''
	json_folder = 'static/json/'
	file = codecs.open(json_folder+json_name+'.json', 'r+','utf-8')
	file_text = file.read()
	file_text = json.loads(file_text)
	return file_text

@app.route('/')
def homepage():
	json_text = readJson("index")
	return render_template('index.html',data=json_text)

@app.route('/<string:student_number>/details')
def intro(student_number):
	json_text = readJson("index")
	student_json ={}
	for student in json_text:
		if student["student_number"] == student_number:
				student_json=student
	return render_template("person.html", data=student_json)

if __name__ == '__main__':
	app.run(debug=True)
	