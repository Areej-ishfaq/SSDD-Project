import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import escape
from urllib.parse import urlparse, urljoin
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from forms import RegistrationForm, LoginForm, TaskForm
from models import db, User, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Rate limiter to prevent brute-force attacks
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def is_safe_url(target):
    """Check if the URL is safe for redirection."""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=escape(form.username.data), password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=escape(form.username.data.strip())).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page and is_safe_url(next_page):
                return redirect(next_page)
            return redirect(url_for('tasks'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(description=escape(form.description.data), user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully.', 'success')
        return redirect(url_for('tasks'))
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', form=form, tasks=tasks)

@app.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('Unauthorized action.', 'danger')
        return redirect(url_for('tasks'))
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully.', 'success')
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

