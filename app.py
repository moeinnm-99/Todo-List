from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
# from notify import send_notification

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.DateTime, nullable=True)



@app.route('/')
def index():
    filter_by = request.args.get('filter', 'all')
    query = Task.query

    if filter_by == 'done':
        query = query.filter_by(done=True)
    elif filter_by == 'pending':
        query = query.filter_by(done=False)

    tasks = query.order_by(Task.deadline.asc().nulls_last()).all()
    total = Task.query.count()
    done = Task.query.filter_by(done=True).count()
    pending = Task.query.filter_by(done=False).count()

    for task in tasks:
        if task.deadline and not task.done and (task.deadline - datetime.utcnow()).total_seconds() < 3600:
            send_notification(f"⚠️ Task nearing deadline: {task.content} (Deadline: {task.deadline})")

    return render_template('index.html', tasks=tasks, total=total, done=done, pending=pending, current_filter=filter_by)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    deadline_str = request.form.get('deadline')
    deadline = datetime.strptime(deadline_str, '%Y-%m-%dT%H:%M') if deadline_str else None
    new_task = Task(content=content, deadline=deadline)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        deadline_str = request.form.get('deadline')
        task.deadline = datetime.strptime(deadline_str, '%Y-%m-%dT%H:%M') if deadline_str else None
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/done/<int:id>')
def mark_done(id):
    task = Task.query.get_or_404(id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
