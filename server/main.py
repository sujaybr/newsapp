from flask import Flask, render_template, request, redirect, url_for, session, jsonify, session
import getCategoryData
from getExtraCategories import getAllCategories
from pymongo import MongoClient
from jinja2 import Template
import requests
import os
import random

app = Flask(__name__)
app.secret_key = "K@isio#)DIg>+ido=giao219KDJF-!"
photos_folder = os.path.join('static','photos')
app.config['upload_folder'] = photos_folder

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']
logged_in = False

def isLoggedIn():
    global logged_in
    return logged_in

# login register page
@app.route("/login", methods=['GET', 'POST'])
def login():
    users = db.users.find()
    global logged_in

    list_of_users = []
    for i in users:
        list_of_users.append(i)

    if request.method == 'POST':
        if request.form['btn'] == "login":
            for i in list_of_users:
                if i['email'] == request.form['lemail']:
                    if i['password'] == request.form['lpsw']:
                        session['email'] = i['email']
                        session['password'] = i['password']
                        logged_in = True
                        return redirect("/category/all")
                    else:
                        return redirect(url_for('login'))    
            return redirect(url_for('login'))
        else:
            for i in list_of_users:
                if i['email'] == request.form['email']:
                    return redirect(url_for('index'))
            email_id = request.form['email']
            password = request.form['psw']
            post = {'email': email_id, 'password': password, 'PositivePriority': [], 'NegativePriority': []}
            session['email'] = email_id
            session['password'] = password

            db.users.insert(post)
            logged_in = True
            return redirect("/category/all")
    else:
        full_filename = os.path.join(app.config['upload_folder'],'login.png')
        return render_template("login.html", login_image=full_filename)

# homepage
@app.route("/", methods=['GET', 'POST'])
def homepage():
    if not isLoggedIn():
        return redirect(url_for("login"))
    return render_template("dashboard.html")

# on successful login or register
@app.route('/dashboard')
def success():
    return render_template('dashboard.html')

# setting priority
@app.route("/priority", methods=['GET', 'POST'])
def priority():
    if not isLoggedIn():
        return redirect(url_for("login"))
    if request.method == 'POST':
        email1 = session.get('email')
        if request.form["btn"] == 'Add':
            existing = db.users.find_one({"email": email1})['PositivePriority']
            valueToUpdate1 = request.form['firstname'].lower()
            existing.append(valueToUpdate1)
            existing = list(set(existing))
            db.users.update({"email": email1}, {"$set": {"PositivePriority": existing}})

            existing_category = db.category.find_one({"id": 0})['category']
            existing_category.append(valueToUpdate1)
            existing_category = list(set(existing_category))
            db.category.update({"id": 0}, {"$set": {"category": existing_category}})
        else:
            existing1 = db.users.find_one({"email": email1})['NegativePriority']
            valueToUpdate2 = request.form['firstname'].lower()
            existing1.append(valueToUpdate2)
            db.users.update({"email": email1}, {"$set": {"NegativePriority": existing1}})
        return redirect(url_for('priority'))
    else:
        email1 = session.get('email')
        existing_positive = db.users.find_one({"email": email1})['PositivePriority']
        existing_negative = db.users.find_one({"email": email1})['NegativePriority']
        existing_positive = list(set(existing_positive))
        existing_negative = list(set(existing_negative))
        return render_template('priority.html', my_positive_list = existing_positive, my_negative_list = existing_negative)


@app.route("/category/<cat>")
def getCategoryNews(cat):
    if not isLoggedIn():
        return redirect(url_for("login"))
    data = getCategoryData.getNewsForCategory(cat)
    email1 = session.get('email')
    existing_positive = db.users.find_one({"email": email1})['PositivePriority']
    existing_positive = list(set(existing_positive))

    temp = []
    for i in data:
        item = {}
        item['title'] = i['title']
        item['description'] = i['description']
        item['url'] = i['url']
        temp.append(item)
    # return jsonify({"data": temp})

    random.shuffle(data)


    core_categories = ['business', 'sports', 'technology', 'entertainment', 'politics','all']
    if cat in core_categories:
        return render_template("categorynews.html", data = temp , cat = cat)
    else:
        return render_template("prioritynews.html", data = temp, my_positive_list = existing_positive)

@app.route("/priority/<cat>")
def getPriorityNews(cat):
    if not isLoggedIn():
        return redirect(url_for("login"))

    data = []
    cats = getAllCategories()
    if cat == 'all':
        for i in cats:
            data += getCategoryData.getNewsForCategory(i)
        random.shuffle(data)
    else:
        data = getCategoryData.getNewsForCategory(cat)

    random.shuffle(data)
    email1 = session.get('email')
    existing_positive = db.users.find_one({"email": email1})['PositivePriority']
    existing_positive = list(set(existing_positive))

    temp = []
    for i in data:
        item = {}
        item['title'] = i['title']
        item['description'] = i['description']
        item['url'] = i['url']
        temp.append(item)

    # return jsonify({"data": temp})
    return render_template("prioritynews.html", data = temp, my_positive_list = existing_positive , cat = cat)

@app.route("/dataToDb")
def putDataToDb():
    data = request.get_json()
    
    data = {}
    for i in data:
        data['title'] = i['title']
        data['description'] = i['description']
        data['url'] = i['url']

        # append to db
        db.newsdata.insert(data)

    return jsonify({"status":True})

# get email
@app.route("/email")
def getEmail():
    return str(session.get('email') + str(isLoggedIn()))

@app.route("/profile")
def profile():
    if not isLoggedIn():
        return redirect(url_for("login"))
    full_filename = os.path.join(app.config['upload_folder'],'login.png')
    return render_template("profile.html", email = session.get('email'), login_image = full_filenameAA)

@app.route("/about")
def about():
    if not isLoggedIn():
        return redirect(url_for("login"))
    full_filename = os.path.join(app.config['upload_folder'],'bitlogo.png')
    return render_template("aboutus.html",bitlogo = full_filename)

@app.route("/mynews")
def myNews():
    if not isLoggedIn():
        return redirect(url_for("login"))
    email1 = session.get('email')
    existing_positive = db.users.find_one({"email": email1})['PositivePriority']
    existing_positive = list(set(existing_positive))
    # data = getCategoryData.getAllCategories('pall')
    return render_template("mynews.html",my_positive_list=existing_positive)

@app.route("/logout")
def logout():
    user = session.get('email')
    # db.session.commit()
    session.clear
    global logged_in
    logged_in = False
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(port = 3000, debug=True)
