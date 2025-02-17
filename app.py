from flask import Flask, render_template, redirect, request, session, url_for, flash
import pymongo 
import bcrypt 
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) 
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Dossier pour stocker les images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client.itmo_wad_hw2
records = db.users

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

def create_user(username, password):
    records.insert_one({
        "username": username,
        "password": password,
        "photo": "default",
        "city": "Not indicated",
        "profession": "Not indicated"

    })

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_record = records.find_one({"username": username})
        if user_record:
            user_password = user_record['password']
            if bcrypt.checkpw(password.encode('utf-8'), user_password):
                session['username'] = username
                session['photo'] = user_record['photo']
                return redirect(url_for("profile"))
            else:
                flash("Invalid password", "error")
                return redirect(url_for("login"))
        else:
            flash("Invalid username", "error")
            return redirect(url_for("login"))
    else:
        return render_template('login.html')

@app.route("/registration", methods = ["GET", "POST"])
def registration_form():
    if request.method == "POST":
        username = request.form.get("username")
        user = records.find_one({'username' : username})
        if user:
            flash("User with this username is exist. Please, try again", "error")
            return render_template('registration.html')
        else:
            password = request.form.get("password")
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            create_user(username, hashed_password)
            flash("Account created! You can now log in", "success")  
            return redirect(url_for("login")) 
    else:
        return render_template('registration.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    user = records.find_one({"username": username})
    if user:
        print(user)
        photo = user['photo']
        city = user['city']
        profession= user['profession']
        return render_template('profile.html', username=username, photo=photo, city=city, profession=profession)

@app.route('/changepasswd', methods=['GET', 'POST'])
def changepasswd():
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        username = session['username']
        user = records.find_one({"username": username})
        if bcrypt.checkpw(old_password.encode('utf-8'), user['password']):
            hash_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            records.update_one({'username': username}, {'$set': {'password': hash_new_password}})
            flash("Password update with success", "success")
            return render_template('profile.html', username=username, photo=user['photo'], city=user['city'], profession=user['profession'])   
        else:
            flash("Incorrect old password", "error")
            return render_template('profile.html', username=username, photo=user['photo'], city=user['city'], profession=user['profession']) 
    else:
        return render_template('profile.html', username=username, photo=user['photo'], city=user['city'], profession=user['profession'])

@app.route('/update', methods = ['GET', 'POST'])
def updateInfo():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user = records.find_one({"username": username})
    
    if request.method == 'POST':
        updates = {}
        city = request.form.get('city')
        if city:
            updates['city'] = city
        profession = request.form.get('profession')
        if profession:
            updates['profession'] = profession
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)  # Sauvegarde du fichier
                updates['photo'] = filepath   
        if updates:
            records.update_one({'username': username}, {'$set': updates})
            flash("Information updated successfully!", "success")
        return redirect(url_for("profile")) 
    return render_template('updateInfo.html', photo=user['photo'], city=user['city'], profession=user['profession'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
