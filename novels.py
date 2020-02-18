from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='0727325535'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username =db.Column(db.String(20),unique=True, nullable=False)
    email =db.Column(db.String(120),unique=True, nullable=False)
    password=db.Column(db.String(60),nullable=False)
    novel=db.relationship('Novel', backref='author',lazy=True)
    
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Novel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(100),unique=True, nullable=False)
    description =db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f"Novel('{self.title}', '{self.description}')"

    
novels=[
    {
    'author':'Carol Nzome',
    'title':'Rich Mum',
    'description':'Women Empowerement',   
    },
    {
    'author':' Eve Grafton',
    'title':'A House To Kill For',
    'description':'In the latest addition, Alice Armstrong’s grandmother, Valerie Newton, pursues an investigation to know more about her heritage. Newton’s name was previously attached to Haskell murdering family and she wanted to know the story behind the Haskell’s “Great House” which was abandoned for so many years',
    
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', novels=novels)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
