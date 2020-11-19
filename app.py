from flask import Flask, render_template, url_for, request, redirect
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


@app.route('/news', methods=['POST', 'GET'])
def news():
    if request.method == "POST":
        car = request.form['car']
        card = request.form['card']
        net = request.form['net']
        gross = request.form['gross']
        tare = request.form['tare']

        sand = Sand(car=car, card=card, net=net, gross=gross, tare=tare)

        try:
            db.session.add(sand)
            db.session.commit()
            return redirect('/')
        except:
            return "При добавлении статьи произошла ошибка"
    else:
        return render_template('news.html')


@app.route('/production')
def production():
    return render_template('production.html')


@app.route('/pit/scales', methods=['POST', 'GET'])
def scales():
    if request.method == "POST":
        return "POST"
    else:
        sum_net = 0.0
        #sand = Sand.query.order_by(Sand.date).all()
        #sand = Sand.query.filter(Sand.car == 'AW-1771b').order_by(Sand.date).all()
        sand = Sand.query.filter(Sand.date >= '2020-11-10').filter(Sand.date <= '2020-11-15').order_by(Sand.date).all()
        for el in sand:
            sum_net = round(sum_net + el.net, 2)
        return render_template('scales.html', sand=sand, sum_net=sum_net)


@app.route('/pit')
def pit():
    return render_template('pit.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'Сотрудники ' + name + ' - ' + str(id)


if __name__ == '__main__':
    app.run(debug=True, host='10.0.0.14', port=80)
