from flask import Flask, render_template, redirect, url_for
from world import World
from city import City

app = Flask(__name__)

# Monde global
world = World()
angelica = City("Angelica", "Smart City")
world.add_city(angelica)

@app.route("/")
def index():
    return render_template("index.html", city=angelica.summary())

@app.route("/tick")
def tick():
    world.tick()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
Add Flask web server
