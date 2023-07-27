from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'users'
}

db_conn = mysql.connector.connect(**db_config)

@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/users')
def users():
    cursor = db_conn.cursor()
    cursor.execute("SELECT id, name, email, role FROM users")
    users_data = cursor.fetchall()
    cursor.close()

    return render_template('users.html', users=users_data)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        cursor = db_conn.cursor()
        cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        db_conn.commit()
        cursor.close()

    return render_template('new_user.html')


@app.route('/users/<int:user_id>')
def user_details(user_id):
    cursor = db_conn.cursor()
    cursor.execute("SELECT id, name, email, role FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()

    if not user_data:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"id": user_data[0], "name": user_data[1], "email": user_data[2], "role": user_data[3]})


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True)

