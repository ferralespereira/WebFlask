from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

# conexion to db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'web_flask'

mysql = MySQL(app)


# context processor
@app.context_processor
def  date_now():
    return {
        'now': datetime.utcnow()
    }

# endPoints


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/information')
@app.route('/information/<string:name>')
def information(name = None):

    text = "<strong>information, do not have a name</strong>"
    if name:
        text = f"<h1>information {name}</h1>"

    return render_template('information.html', 
                            text=text
                            )




@app.route('/contact')
@app.route('/contact/<redirection>')
def contact(redirection = None):
   
    text = "<h1>contact</h1>"
    if redirection:
        return render_template('contact.html', 
                            text=text
                            )
    else:
        return redirect(url_for('information'))


@app.route('/create-car')
def create_car():

    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO cars VALUES(NULL, 'Lambo', 'Gallardo', '100000', 'Los Angeles')")
        cursor.connection.commit()

        return redirect(url_for('index'))

    return render_template('create_car.html', text='lola')

if __name__ == '__main__':
    app.run(debug=True)

