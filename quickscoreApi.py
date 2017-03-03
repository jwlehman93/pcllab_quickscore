from pcllab_quickscore import quickscore
import time
import flask
from flask import Flask, jsonify, request, render_template

start_time = time.time();
qapi = quickscore("GoogleNews-vectors-negative300.bin")
end_time = time.time();
print "Model Initialized in " + str(end_time-start_time) + " seconds\n"

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Hello World</h1>"	

@app.route("/api",  methods=['GET', 'POST'])
def appApi():
	target = request.args.get('target')
	response = request.args.get('response')
	if (((response is None) or (not response)) and ((response is None) or (not response))): 
		ret = render_template('form.html')
	else :
		global qapi
		score = qapi.w2vScore(response, target)
		ret = "target : "+str(target)+"<br>response : "+str(response)+"<br>"
		ret = ret + str(score)
	return ret
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)




#
#target = "because they can eat or use them for camouflage"
#responses = ["because some animals eat algae and green plant, some fish use green plant for camouflage.",
#	"they can blend into them",
#	"they look like food to eat",
#	"they feed from them",
#	"there are good stuff in it for them",
#	"It's bright"]

#for response in responses:
#	score = qapi.w2vScore(response, target)
#	print "\tResponse : " + response + "\n\t Score : "+str(score) 	

