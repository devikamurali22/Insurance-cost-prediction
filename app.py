import flask
from flask import Flask,request,render_template
import joblib

app=Flask(__name__,template_folder='template')
model = joblib.load('deployment123.pkl')

@app.route("/")
def sendindex():
	return render_template("index.html")

@app.route("/predict", methods=["GET","POST"])
def sendpredict():
	if request.method=="POST":
	
	 Age = int(request.form.get('Age'))
	 Sex = request.form.get('Sex')
	 BMI = float(request.form.get('BMI'))
	 Children = request.form.get('Children')
	 Smoker = request.form.get('Smoker')
	 Region = request.form.get('Region')
	
	 prediction=model.predict([[Age,Sex,BMI,Children,Smoker,Region]])
	output=round(prediction[0],2)
	return render_template('predict.html',prediction_text ="Predicted amount.{0:.3f}".format(output))
	

if __name__ == "__main__":
    app.run(debug=True)


	 