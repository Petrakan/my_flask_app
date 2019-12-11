from flask import Flask, render_template, url_for, flash, redirect
from config import Configuration

from forms import RegistrationForm, LoginForm

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)



posts = [
    {
        'author':'Alexey Petrakov',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'December 11, 2019 ',
    },
    {
        'author':'Galina Petrakova',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'November 25, 2019 ',
    },
    {
        'author':'Viktoria Spirina',
        'title':'Blog Post 3',
        'content':'Third post content',
        'date_posted':'August 15, 2019 ',
    }
]


@app.route('/')
def home_page():
    return render_template('home_page.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register' methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Аккаунт создан для {}!'.format(form.username.data), 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title ='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title ='Login', form=form)



if __name__ == '__main__':
    app.run()