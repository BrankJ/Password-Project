from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Tells Flask to load templates/index.html

if __name__ == '__main__':
    app.run(debug=True)  # debug=True auto-reloads when you save changes
