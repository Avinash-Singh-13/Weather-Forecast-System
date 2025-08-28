from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('weather_app.html') 

if __name__ == '__main__':
    app.run(debug=True)
