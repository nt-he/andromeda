from flask import Flask, render_template, request, jsonify, make_response
import os.path, os

from flask.helpers import send_from_directory
app = Flask(__name__)

class Mii:
    def __init__(self, did, file):
        self.did = did
        self.file = file
    def get_discord_id(self):
        return self.did
    def get_file(self):
        return self.file
    def get_full_path(self):
        return os.path.join("miis", self.file)

@app.route('/')
def home():
    return render_template("home.html.jinja2")
@app.route("/load")
def load_miis():
        miis = [f for f in os.listdir("miis") if os.path.isfile(os.path.join("miis", f))]
        if request.args:
            page = int(request.args.get("page"))
            if page == 0:
                return {"miis": miis[0:10]}
            elif page == len(miis):
                return make_response(jsonify({"miis": []})) # I decided to pick this code because I had no clue about anything in the HTTP spec that would make sense.
            else:
                return {"miis": miis[page: page + 10]}
        else:
            return make_response({}, 400)
        
if __name__ == "__main__":
    # In production, these are served by a reverse proxy.
    app.static_folder = "static"
    app.static_url_path = "/static"
    @app.route("/miis/<file>")
    def miis(file):
        return send_from_directory("miis", file)
    app.run(debug=True)