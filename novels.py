from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='0727325535'

novels=[
    {
    'author':'Bettyb',
    'title':'Rich Mum',
    'content':'Women Empowerment',   
    },
    {
    'author':' Eve Grafton',
    'title':'A House To Kill For',
    'content':'In the latest addition, Alice Armstrong’s grandmother, Valerie Newton, pursues an investigation to know more about her heritage. Newton’s name was previously attached to Haskell murdering family and she wanted to know the story behind the Haskell’s “Great House” which was abandoned for so many years',
    
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
