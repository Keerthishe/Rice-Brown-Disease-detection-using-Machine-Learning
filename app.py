from flask import Flask, render_template, request, redirect, session, send_file
from werkzeug.utils import secure_filename
import os, sqlite3, hashlib
from utils import predict_disease, generate_pdf_report, CLASS_NAMES, get_remedy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'static/uploaded'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# === DB Initialization ===
def init_db():
    with sqlite3.connect("users.db") as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
init_db()

# === Routes ===
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password_hash = hashlib.sha256(request.form['password'].encode()).hexdigest()
        with sqlite3.connect("users.db") as conn:
            try:
                conn.execute("INSERT INTO users VALUES (?, ?)", (username, password_hash))
                return redirect('/login_page')
            except:
                return render_template('signup.html', error="Username already exists!")
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_hash = hashlib.sha256(request.form['password'].encode()).hexdigest()
        with sqlite3.connect("users.db") as conn:
            user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", 
                                (username, password_hash)).fetchone()
            if user:
                session['username'] = username
                return redirect('/dashboard')
        return render_template('login.html', error="Invalid credentials")
    # GET request - show form
    return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/')  # not logged in → home
    return render_template('dashboard.html', username=session['username'])

@app.route('/predict', methods=['POST'])
def predict():
    if 'username' not in session:
        return redirect('/')

    file = request.files['image']
    if not file or file.filename == '':
        return "No image selected"

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    disease, confidence, all_probs = predict_disease(filepath)
    remedy = get_remedy(disease)  # Always returns full dict now

    session['prediction'] = {
        'username': session['username'],
        'filename': filename,
        'disease': disease,
        'confidence': confidence,
        'remedy': remedy,
        'values': all_probs
    }

    return render_template('result.html',
                           image=filename,
                           disease=disease,
                           confidence=confidence,
                           remedy=remedy,
                           labels=CLASS_NAMES,
                           values=all_probs)

@app.route('/report')
def report():
    if 'prediction' not in session:
        return redirect('/dashboard')
    filepath = generate_pdf_report(session['prediction'])
    return send_file(filepath, as_attachment=True)

@app.route('/confidence-chart')
def confidence_chart():
    if 'prediction' not in session:
        return redirect('/dashboard')
    data = session['prediction']
    return render_template('confidence_chart.html',
                           labels=CLASS_NAMES,
                           values=data.get('values', []),
                           disease=data['disease'],
                           confidence=data['confidence'])

@app.route('/result')
def result():
    if 'prediction' not in session:
        return redirect('/dashboard')
    data = session['prediction']
    return render_template('result.html',
                           image=data['filename'],
                           disease=data['disease'],
                           confidence=data['confidence'],
                           remedy=data['remedy'],
                           labels=CLASS_NAMES,
                           values=data['values'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)