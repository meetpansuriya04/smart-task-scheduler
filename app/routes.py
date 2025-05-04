from flask import Blueprint, request, jsonify
from .models import Task, db

main = Blueprint('main', __name__)

@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(
        title=data['title'],
        description=data.get('description'),
        due_date=data.get('due_date')
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201

@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in tasks])
