from flask import Flask, jsonify
from flask import render_template, redirect, request, url_for, session
from pymongo import MongoClient
import requests

app = Flask(__name__)
app.secret_key = 'secret123'

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/userlogin', methods=['POST', 'GET'])
def userlogin():
    users = db.users.find()

    list_of_users = []
    for i in users:
        list_of_users.append(i)

    if request.method == 'POST':
        for i in list_of_users:
            if i['email'] == request.form['email']:
                if i['password'] == request.form['psw']:
                    session['email'] = i['email']
                    session['password'] = i['password']
                    return redirect(url_for('success'))
                else:
                    return redirect(url_for('index'))    
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/userregistration', methods=['POST', 'GET'])
def userregistration():
    users = db.users.find()

    list_of_users = []
    for i in users:
        list_of_users.append(i)

    if request.method == 'POST':
        for i in list_of_users:
            if i['email'] == request.form['email']:
                return redirect(url_for('index'))
        email_id = request.form['email']
        password = request.form['psw']
        post = {'email': email_id, 'password': password, 'PositivePriority': [], 'NegativePriority': []}
        session['email'] = email_id
        session['password'] = password

        db.users.insert(post)
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))


@app.route('/priority', methods=['POST', 'GET'])
def priority():
    if request.method == 'GET':
        return redirect(url_for('goToPriority'))

@app.route('/Priority', methods=['POST', 'GET'])
def Priority():
    if request.method == 'POST':
        email1 = session.get('email')
        if request.form["btn"] == 'Add':
            existing = db.users.find_one({"email": email1})['PositivePriority']
            valueToUpdate1 = request.form['firstname']
            existing.append(valueToUpdate1)
            existing = list(set(existing))
            db.users.update({"email": email1}, {"$set": {"PositivePriority": existing}})

            existing_category = db.category.find_one({"id": 0})['category']
            existing_category.append(valueToUpdate1)
            existing_category = list(set(existing_category))
            db.category.update({"id": 0}, {"$set": {"category": existing_category}})
        else:
            existing1 = db.users.find_one({"email": email1})['NegativePriority']
            valueToUpdate2 = request.form['firstname']
            existing1.append(valueToUpdate2)
            db.users.update({"email": email1}, {"$set": {"NegativePriority": existing1}})
        return redirect(url_for('goToPriority'))
    else:
        return redirect(url_for("goToPriority"))


@app.route('/success')
def success():
    return render_template('newsfeeds.html')


@app.route('/goToPriority')
def goToPriority():
    email1 = session.get('email')
    existing_positive = db.users.find_one({"email": email1})['PositivePriority']
    existing_negative = db.users.find_one({"email": email1})['NegativePriority']
    existing_positive = list(set(existing_positive))
    existing_negative = list(set(existing_negative))
    return render_template('priority.html', my_positive_list = existing_positive, my_negative_list = existing_negative)


@app.route("/category/<cat>")
def category(cat):
    r = requests.get("https://newsapi.org/v2/everything?q=" + cat + "&sortBy=publishedAt&apiKey=e8704cf44921496593e63fc898537993")
    item = {"articles": r.json()['articles']}
    return jsonify({"data": item})


if __name__ == '__main__':
    app.run(debug=True)
