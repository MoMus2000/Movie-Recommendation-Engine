from flask import Flask, request, redirect
import os
from flask import render_template
from generate_predictions import process_result
from images import get_image_pics


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
	return 'Pls visit proper endpoint to see your movie predictions'

@app.route("/", methods=['GET','POST'])
def home():
	if(request.method == "POST"):
		search_result = request.form.get("search_query").lower()
		vals,title = process_result(search_result)
		if(len(vals)) == 0:
			return render_template('index.html',title="search result not found please try again")
		images = get_image_pics(vals)
		print(images)
		test = zip(vals,images)
		print(vals)
		return render_template("index.html",your_list=vals,title=list(title)[0],image_pics=images,test=test )
	else:
		return render_template('index.html',title='')

@app.route("/hindi", methods=['GET','POST'])
def home_hindi():
	if(request.method == "POST"):
		search_result = request.form.get("search_query").lower()
		vals,title = process_result(search_result,hindi=True)
		if(len(vals)) == 0:
			return render_template('index.html',title="search result not found please try again")
		images = get_image_pics(vals,hindi=True)
		print(images)
		test = zip(vals,images)
		print(vals)
		return render_template("index.html",your_list=vals,title=list(title)[0],image_pics=images,test=test )
	else:
		return render_template('index.html',title='')



if __name__ == "__main__":
	app.run(debug=True)

# else:
# 	url = ngrok.connect(5000)
# 	print("TUNNEL URL:", url)

# if __name__ =="__main__":
	# app.run(debug=True,host='0.0.0.0', port=8000)