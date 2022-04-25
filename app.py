from flask import Flask , render_template , request
import pickle
import numpy as np
app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index2.html")

@app.route("/submit",methods=["POST"])
def submit():
	if request.method == "POST":
		area = request.form["area"]
		bedrooms = request.form["bedrooms"]
		bathrooms = request.form["bathrooms"]
		parking = request.form["parking"]
		location = request.form["Location"]
		inputList = [bedrooms,area,bathrooms,parking,location]
		with open("model.pkl", 'rb') as file:
			pickle_model = pickle.load(file)
			y_pred_from_pkl = pickle_model.predict([inputList])
	return render_template("result.html",prediction = y_pred_from_pkl)  

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__=="__main__":
    app.run(debug=True)