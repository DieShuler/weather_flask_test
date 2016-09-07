# First simple flask app

from flask import Flask, render_template, request
import os
import weather

app = Flask(__name__)

@app.route("/")
def index():
    name = request.values.get('name')
    location = request.values.get('location')
    forecast = None
    if location:
        forecast = weather.get_weather(location)
    return render_template('index.html', location=location, forecast=forecast)

@app.route("/about.html")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
