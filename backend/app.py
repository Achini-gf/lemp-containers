from flask import Flask, jsonify
import os
import pymysql

app = Flask(__name__)

@app.get("/api")
def root_api():
    return jsonify({"message": "Hello from Flask API 👋", "status": "ok"})

@app.get("/api/ping")
def ping():
    return jsonify({"pong": True})

@app.get("/api/db")
def db_check():
    cfg = {
        "host": os.getenv("DB_HOST", "db"),
        "port": int(os.getenv("DB_PORT", 3306)),
        "user": os.getenv("DB_USER", "appuser"),
        "password": os.getenv("DB_PASSWORD", "apppass"),
        "database": os.getenv("DB_NAME", "appdb"),
        "cursorclass": pymysql.cursors.DictCursor,
    }
    try:
        with pymysql.connect(**cfg) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, message FROM hello_messages LIMIT 1;")
                row = cur.fetchone()
                return jsonify({"db": "connected", "sample": row}), 200
    except Exception as e:
        return jsonify({"db": "unavailable", "error": str(e)}), 500

# gunicorn looks for 'app'
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)