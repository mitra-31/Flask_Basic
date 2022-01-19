from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student'
mysql = MySQL(app)

@app.route('/hello')
def homepage():
    return render_template("home.html")



@app.route('/',methods=['GET', 'POST'])
def login():
  
    if request.method == 'POST':
        error = None
        
        # Data extracted from the login.html page.   
        # We get username and password from that page.
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        
        # Creating mySql instance object.
        # cur = mysql.connection.cursor()
        
        # Reterving all the username and password from Database. 
        # cur.execute("SELECT user_id,username,password FROM users WHERE username = '{0}'".format(username))
        
        # Assinging the output of the above query to variable called user
        # user variable will be type of tuple
        # user = (user_id,username,password)
        # user = cur.fetchone()
        
        
        # Authentication Process, We check the username and password is correct.
        # If its true then it redirects to url "/dashboard".
        # if user[1] == username and  user[1] == password:
        #     return redirect('/dashboard')
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT std_id,std_name,std_course,std_year,std_address,std_gender FROM student")
    std = cur.fetchall()
    # print(std)
    return render_template('dashboard.html',students=std)




@app.route('/add',methods=['POST','GET'])
def add():
    if request.method == 'POST':
        std_name = request.form.get('std_name')
        std_course = request.form.get('std_course')
        std_year = request.form.get('std_year')
        std_address = request.form.get('std_address')
        std_gender = request.form.get('std_gender')
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO student(std_name,std_course,std_year,std_address,std_gender) VALUES(%s,%s,%s,%s,%s)"""
                    ,(std_name,std_course,std_year,std_address,std_gender))
        mysql.connection.commit()
    return redirect('dashboard')

@app.route('/update/<int:user_id>',methods=['POST'])
def update(user_id):

    cur = mysql.connection.cursor()
    cur.execute("SELECT std_name,std_course,std_year,std_address,std_id FROM student WHERE std_id = '{0}'".format(user_id))
    std = cur.fetchone()
    if request.method == 'POST':
      
        std_name = request.form.get('std_name')
        std_course = request.form.get('std_course')
        std_year = request.form.get('std_year')
        std_address = request.form.get('std_address')
        cur = mysql.connection.cursor()
        # UPDATE `student` SET `std_name` = 'Mitra', `std_course` = 'CSE', `std_year` = '4', `std_address` = 'Bellary' WHERE `student`.`std_id` = 1;
        cur.execute("""UPDATE student
                        SET std_name = '{0}', std_course = '{1}',
                        std_year = '{2}', std_address = '{3}'
                        WHERE std_id = '{4}'""".format(std_name,std_course,std_year,std_address,user_id))
        mysql.connection.commit()
    return render_template("update.html",students=std)


@app.route('/delete/<int:user_id>',methods=['POST', 'GET'])
def delete(user_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)