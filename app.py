from flask import Flask
from database import Postgres

app = Flask(__name__)
db = Postgres('db', 5432, 'database', 'username', 'password')


@app.route('/')
def hello():
    db.create_user("test", "test")
    return "Hello world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)