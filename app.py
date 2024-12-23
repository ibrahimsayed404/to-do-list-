from flask import Flask, render_template, request, redirect, url_for
import db  # Import database module

app = Flask(__name__)

# Initialize the database explicitly at the start of the app
db.init_db()

@app.route('/')
def index():
    tasks = db.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    db.add_task(task_name)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def mark_complete(task_id):
    db.update_task_status(task_id, 'complete')
    return redirect(url_for('index'))

@app.route('/incomplete/<int:task_id>', methods=['POST'])
def mark_incomplete(task_id):
    db.update_task_status(task_id, 'incomplete')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    db.delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
