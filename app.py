from flask import Flask, jsonify
from NitrotypePy import user


app = Flask(__name__) 

@app.route("/")
def home():
    return "Nitro Type Alerts Bot is running!"

@app.route("/track/<username>")
def track(username):
    try:
        racer_data = user(username)
        
        return jsonify({
            "username": player.username,
            "speed": player.speed,
            "races_completed": player.races_completed,
            "team": player.team
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5000)
