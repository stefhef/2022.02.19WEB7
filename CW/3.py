from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        return render_template("training.html", title="Инженерные тренажеры",
                               image=url_for('static', filename='img/ing.png'))
    else:
        return render_template("training.html", title="Научные симуляторы",
                               image=url_for('static', filename='img/other.png'))


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    lst = (
    "инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию", "климатолог",
    "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения", "метеоролог",
    "оператор марсохода", "киберинженер", "штурман", "пилот дронов")

    return render_template("profession.html", title="Страничка", lst=lst, list_type=list_type)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')