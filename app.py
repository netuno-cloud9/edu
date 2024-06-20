from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PORT'] = 3307  # Specify the MySQL port
app.config['MYSQL_PASSWORD'] = 'BASH$634pcpv!!'
app.config['MYSQL_DB'] = 'edu_db'

mysql = MySQL(app)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['logged_in'] = True
            session['username'] = username
            session['name'] = user[1]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))

# Main route
@app.route('/')
def index():
    if 'logged_in' in session:
        name = session.get('name')
        return render_template('index.html', name=name)
    else:
        return redirect(url_for('login'))
    
# Route for splinks.html
@app.route('/splinks')
def splinks():
    return render_template('splinks.html')
# Other routes...
# Add your other routes here

if __name__ == '__main__':
    app.run(debug=True)
