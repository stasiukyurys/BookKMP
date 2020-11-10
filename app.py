from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/help')
def help_user():
    return render_template('help.html')


@app.route('/abk')
def abk():
    return render_template('abk.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/production')
def production():
    return render_template('production.html')


@app.route('/pit')
def pit():
    return render_template('pit.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'Сотрудники ' + name + ' - ' + str(id)


if __name__ == '__main__':
    app.run(debug=True)
