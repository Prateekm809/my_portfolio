from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Anjali@007"
app.config['MYSQL_DB'] = "adit"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    success_message = None

    if request.method == "POST":
        name = request.form['name']
        subject = request.form['subject']
        email = request.form['email']
        message = request.form['message']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cv (name, subject, email, message) VALUES (%s, %s, %s, %s)", (name, subject, email, message))
        mysql.connection.commit()
        cur.close()
        
        success_message = "We have recorded Your response!!!!!"

    return render_template('index.html', success_message=success_message)

if __name__ == "__main__":
    app.run(debug=True)

