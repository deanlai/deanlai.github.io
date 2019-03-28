from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/')
@app.route('/tidbits')
def tidbits():
    return render_template('tidbits.html')


@app.route('/places')
def places():
    return render_template('places.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/energy')
def energy():
    return render_template('energy.html')


@app.route('/pink')
def pink():
    return render_template('pink.html')


@app.route('/oregon')
def oregon():
    return render_template('oregon.html')


@app.route('/entropy')
def entropy():
    return render_template('entropy.html')


if __name__ == '__main__':
    app.run(debug=True)