from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode=request.form['zip']
	r=requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=a7abb35f092326889eb7ccd221ff9c03')
	json_object=r.text
	return json_object


	
@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)
	 
	app = flask_app.wsgi_app