from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():	
	zipcode=request.form['zip']
	r=requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=a7abb35f092326889eb7ccd221ff9c03')
	
	Cityname=request.form['city_name']
	r=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+Cityname+',uk&appid=a7abb35f092326889eb7ccd221ff9c03')
	
	json_object=r.json()
	temp_k=float(json_object['main']['temp'])	
	temp_f=(temp_k-273.15)*1.8+32
	
	temp_v=float(json_object['main']['temp_max'])
	temp_f1=(temp_v-273.15)*1.8+32
	
	temp_min=(json_object['main']['temp_min'])
	temp_o=(temp_min-273.15)*1.8+32
	
	humidity=(json_object['main']['humidity'])
	pressure=(json_object['main']['pressure'])
	
	return render_template('temperature.html', temp=temp_f,temp_max=temp_f1, temp_min=temp_o, humidity=humidity, pressure=pressure)
	
	
	
@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)
	
