from flask import Flask
import os

app =Flask(__name__)

from flask import Flask, request, render_template

import urllib2, json

app = Flask(__name__)

@app.route('/')
def location():
	return render_template('location.html')
	    

@app.route('/weather', methods=['POST',"GET"])
def weather():

	if request.method=='POST':
		result=request.form
		print type(result)
		list_loc=[]
		print result['City'],result['State']
		state=result['State']
		city=result['City']
		f=urllib2.urlopen('http://api.wunderground.com/api/f3c442098e60ca9c/conditions/q/'+state+'/'+city+'.json')
		list_loc.append(city)
		list_loc.append(state)
		json_string=f.read()
		parsed_json=json.loads(json_string)
		#print parsed_json
		weather=parsed_json['current_observation']['weather']
		temp=parsed_json['current_observation']['temperature_string']
		humid=parsed_json['current_observation']["relative_humidity"]
		wind=parsed_json['current_observation']["wind_string"]
		wind_mph=parsed_json['current_observation']["wind_mph"]
		
		list_loc.append(weather)
		list_loc.append(temp)
		list_loc.append(humid)
		list_loc.append(wind)
		list_loc.append(wind_mph)
		return render_template('weather.html',result=list_loc)    

if __name__=="__main__":
	
	app.run(host="0.0.0.0", port=5000,debug=True)
