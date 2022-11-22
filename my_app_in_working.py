import sqlite3
from flask import Flask, redirect, render_template,request,url_for,flash
from werkzeug.exceptions import abort
def get_db_connection():
    conn=sqlite3.connect('database.db')
    conn.row_factory=sqlite3.Row
    return conn
    
def get_post(post_id):
    conn=get_db_connection()
    post = conn.execute('select * from posts where id = ?',(post_id,)).fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_all_posts():
    conn=get_db_connection()
    posts=conn.execute("select * from posts").fetchall()
    conn.close()
    return posts

app = Flask(__name__)
app.config['SECRET_KEY']='My Key'
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route("/register",methods=('GET','POST'))
def regist():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        birthday=request.form['birthday']
        if  username is None:
            flash('username is required!')
        elif email is None:
            flash('email is required!')
        else:
            conn = get_db_connection()
            conn.execute('insert or replace into users values (?,?,?,?,?);',(username,email,firstname,lastname,birthday))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('regstration.html')
@app.route('/login')
def login():
    error = None
    conn = get_db_connection()
    if request.method == 'POST':
        psw=conn.execute("select psw from users where username = ?",request.form['username']).fetchall()
        psw=psw[0]
        print(psw)
        if psw is None:
            error = 'Invalid username'
        elif psw != request.form['psw']:
            error = 'Invalid password'
        else:
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/main')
def index():
    conn=get_db_connection()
    posts=conn.execute('select * from posts').fetchall()
    conn.close()
    return render_template('index.html',posts=posts)

@app.route('/main/<int:id>/post',methods=('GET','POST'))
def post(id):
    my_post = get_post(id)
    return render_template('post.html',post=my_post)

@app.route('/main/create',methods=('GET','POST'))
def create():
    if request.method=='POST':
        title=request.form['title']
        content=request.form['content']
        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('insert into posts (title , content) values (?,?)',(title,content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')
@app.route('/main/<int:id>/edit',methods=('GET','POST'))
def edit(id):
    post = get_post(id)
    if request.method=='POST':
        title=request.form['title']
        content = request.form['content']
        if not title:
            flash('Ttle is required!')
        else:
            conn = get_db_connection()
            conn.execute('Update posts set title = ? ,content = ? where id = ?',(title,content,id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html',post=post)


@app.route('/main/<int:id>/delete', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
