from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_cap = StringField('Id капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'nknrugjnjrnhgijekmgikjriohjieigmejgk;nemvstepaloxh8ekjbfbejbf<3'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', title='Distribution',
                           css_file=url_for('static', filename='css/distribution.css'),
                           humans=['Peolpe 1', 'people2', 'Stepan Melnicov'])


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
        "инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения", "метеоролог",
        "оператор марсохода", "киберинженер", "штурман", "пилот дронов")

    return render_template("profession.html", title="Страничка", lst=lst, list_type=list_type)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    d = {"surname": "Sur",
         "name": "Stepan",
         "ed": "Up average",
         "prof": "Pilot",
         "sex": "male",
         "mot": "I hope it",
         "ready": "True"}
    return render_template('answer.html', title='Ответик', d=d)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('form.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
