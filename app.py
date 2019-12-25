from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='dheerajrocks123#45'
app.config['MYSQL_DB']='flask'
mysql=MySQL(app)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        u=request.form
        name=u['name']
        email=u['email']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO flask_table1(name,email) VALUES(%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return "SUCCESS"
    else:
        return render_template('application.html')
@app.route('/users')
def users():
    c=mysql.connection.cursor()
    count=c.execute("select * from flask_table1")
    if count>0:
        det=c.fetchall()
        return render_template('usrs.html',details=det)
app.run(host='0.0.0.0')

