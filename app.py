# TASK 1 continued
from flask import Flask, request, jsonify
import mysql.connector
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        database=app.config['MYSQL_DATABASE'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD']
    )
    return conn

# TASK 2
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Members (name, email, phone) VALUES (%s, %s, %s)",
        (data['name'], data['email'], data['phone'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Member added successfully!'}), 201

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()
    if member:
        return jsonify(member), 200
    else:
        return jsonify({'message': 'Member not found!'}), 404
    
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Members SET name = %s, email = %s, phone = %s WHERE id = %s",
        (data['name'], data['email'], data['phone'], id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Member updated successfully!'}), 200

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Members WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Member deleted successfully!'}), 200

#TASK 3
@app.route('/workout_sessions', methods=['POST'])
def schedule_session():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO WorkoutSessions (member_id, session_date, session_type) VALUES (%s, %s, %s)",
        (data['member_id'], data['session_date'], data['session_type'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Workout session scheduled!'}), 201

@app.route('/workout_sessions/<int:id>', methods=['PUT'])
def update_session(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE WorkoutSessions SET session_date = %s, session_type = %s WHERE id = %s",
        (data['session_date'], data['session_type'], id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Workout session updated!'}), 200

@app.route('/workout_sessions/<int:member_id>', methods=['GET'])
def get_sessions(member_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM WorkoutSessions WHERE member_id = %s", (member_id,))
    sessions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(sessions), 200

if __name__ == '__main__':
    app.run(debug=True)