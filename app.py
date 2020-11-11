from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BookKMP.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Sand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car = db.Column(db.String(100), nullable=False)         # имя авто
    card = db.Column(db.String(20), nullable=False)         # id карты
    date = db.Column(db.DateTime, default=datetime.utcnow)  # дата взвешивания
    time = db.Column(db.DateTime, default=datetime.utcnow)  # время взвешивания
    net = db.Column(db.Float, nullable=False)               # нетто
    gross = db.Column(db.Float, nullable=False)             # брутто
    tare = db.Column(db.Float, nullable=False)              # тара - вес авто

    def __repr__(self):
        return '<Sand %r>' % self.id


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


@app.route('/pit/scales')
def scales():
    sand = Sand.query.order_by(Sand.date).all()
    return render_template('scales.html', sand=sand)


@app.route('/pit')
def pit():
    return render_template('pit.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'Сотрудники ' + name + ' - ' + str(id)


if __name__ == '__main__':
    app.run(debug=True)
