from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Get the path to the SQLite database file
DB_FILE_PATH = os.path.join(os.getcwd(), 'data', 'example.db')

@app.route('/data', methods=['GET'])
def get_data():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_FILE_PATH)
    c = conn.cursor()

    # Retrieve data from the database
    c.execute("SELECT * FROM data")
    data = c.fetchall()

    # Close the database connection
    conn.close()

    return jsonify({'data': data})

@app.route('/data', methods=['POST'])
def add_data():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_FILE_PATH)
    c = conn.cursor()

    # Add data to the database
    value = request.json.get('value')
    c.execute("INSERT INTO data (value) VALUES (?)", (value,))
    conn.commit()

    # Close the database connection
    conn.close()

    return jsonify({'message': 'Data added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
