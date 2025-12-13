"""
Flask REST API - Python equivalent to Node.js Express
Complete CRUD API with JWT Authentication
"""

from flask import Flask, request, jsonify
from flask.views import MethodView
from functools import wraps
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Use environment variable in production

# In-memory storage (use database in production)
users_db = {}
todos_db = {}
todo_id_counter = 0


def token_required(f):
    """JWT Authentication decorator"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Remove 'Bearer ' prefix if present
            if token.startswith('Bearer '):
                token = token[7:]
            
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated


@app.route('/api/register', methods=['POST'])
def register():
    """User registration"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    
    if username in users_db:
        return jsonify({'message': 'User already exists'}), 400
    
    users_db[username] = {
        'password': generate_password_hash(password),
        'created_at': datetime.datetime.utcnow().isoformat()
    }
    
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/api/login', methods=['POST'])
def login():
    """User login - returns JWT token"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    
    user = users_db.get(username)
    
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    # Generate JWT token
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, app.config['SECRET_KEY'], algorithm='HS256')
    
    return jsonify({
        'token': token,
        'message': 'Login successful'
    }), 200


@app.route('/api/todos', methods=['GET'])
@token_required
def get_todos(current_user):
    """Get all todos for current user"""
    user_todos = [todo for todo in todos_db.values() if todo['user'] == current_user]
    return jsonify(user_todos), 200


@app.route('/api/todos', methods=['POST'])
@token_required
def create_todo(current_user):
    """Create a new todo"""
    global todo_id_counter
    
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    
    if not title:
        return jsonify({'message': 'Title is required'}), 400
    
    todo_id_counter += 1
    new_todo = {
        'id': todo_id_counter,
        'title': title,
        'description': description,
        'completed': False,
        'user': current_user,
        'created_at': datetime.datetime.utcnow().isoformat()
    }
    
    todos_db[todo_id_counter] = new_todo
    return jsonify(new_todo), 201


@app.route('/api/todos/<int:todo_id>', methods=['GET'])
@token_required
def get_todo(current_user, todo_id):
    """Get a specific todo"""
    todo = todos_db.get(todo_id)
    
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404
    
    if todo['user'] != current_user:
        return jsonify({'message': 'Unauthorized'}), 403
    
    return jsonify(todo), 200


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
@token_required
def update_todo(current_user, todo_id):
    """Update a todo"""
    todo = todos_db.get(todo_id)
    
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404
    
    if todo['user'] != current_user:
        return jsonify({'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    todo['title'] = data.get('title', todo['title'])
    todo['description'] = data.get('description', todo['description'])
    todo['completed'] = data.get('completed', todo['completed'])
    
    return jsonify(todo), 200


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    """Delete a todo"""
    todo = todos_db.get(todo_id)
    
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404
    
    if todo['user'] != current_user:
        return jsonify({'message': 'Unauthorized'}), 403
    
    del todos_db[todo_id]
    return jsonify({'message': 'Todo deleted'}), 200


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)

