
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Channel + playlist IDs
CHANNEL_URL = "https://www.youtube.com/shubhamgourtech"
PLAYLISTS = {
    "jenkins": {
        "title": "🧩 Jenkins Playlist",
        "list_id": "PLBr8obKbpkYvJEaPmrzhHhwx8uPj8WYbg",
        "gradient": "linear-gradient(135deg, #ff0844 0%, #ffb199 100%)"
    },
    "docker": {
        "title": "🐳 Docker Playlist",
        "list_id": "PLBr8obKbpkYsFtSF1XY9rM_3LH8LKRwSw",
        "gradient": "linear-gradient(135deg, #00c6ff 0%, #0072ff 100%)"
    },
    "github": {
        "title": "💻 GitHub Playlist",
        "list_id": "PLBr8obKbpkYt679NgO1KqZOoY_QYYLBl2",
        "gradient": "linear-gradient(135deg, #8e2de2 0%, #4a00e0 100%)"
    },
    "aws": {
        "title": "☁️ AWS Playlist",
        "list_id": "PLBr8obKbpkYtn5eIK3iTgiV7MSgFwO-tr",
        "gradient": "linear-gradient(135deg, #f7971e 0%, #ffd200 100%)"
    }
}

@app.context_processor
def inject_globals():
    return {"CHANNEL_URL": CHANNEL_URL, "PLAYLISTS": PLAYLISTS}

@app.route("/")
def index():
    # Build cards from PLAYLISTS
    cards = [
        {"key": k, "title": v["title"], "url": f"/{k}"}
        for k, v in PLAYLISTS.items()
    ]
    return render_template("index.html", cards=cards)

@app.route("/jenkins")
def jenkins():
    p = PLAYLISTS["jenkins"]
    return render_template("playlist.html", title=p["title"], list_id=p["list_id"], gradient=p["gradient"])

@app.route("/docker")
def docker():
    p = PLAYLISTS["docker"]
    return render_template("playlist.html", title=p["title"], list_id=p["list_id"], gradient=p["gradient"])

@app.route("/github")
def github():
    p = PLAYLISTS["github"]
    return render_template("playlist.html", title=p["title"], list_id=p["list_id"], gradient=p["gradient"])

@app.route("/aws")
def aws():
    p = PLAYLISTS["aws"]
    return render_template("playlist.html", title=p["title"], list_id=p["list_id"], gradient=p["gradient"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
