from application import app,db 
from flask import render_template,request,jsonify
from application.models import Users

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    result = Users.objects.filter(name__startswith=searchbox)
    return jsonify(result)