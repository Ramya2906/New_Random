from flask import Flask, render_template

app = Flask(__name__)


@app.route('/checking')
def home():
    return render_template('checking.html')

if __name__ == "__main__":
    app.run(debug=True)


