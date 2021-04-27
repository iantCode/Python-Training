from flask import Flask
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connected")
def connect_handler():
    socketio.emit("response", {"nickname":"", "message": "새로운 유저 입장"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=6326, debug=True)