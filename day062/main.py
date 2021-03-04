from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    open_time = StringField('Open', validators=[DataRequired()])
    close_time = StringField('Close', validators=[DataRequired()])

    coffee = SelectField('Coffee', choices=[
        ('0', '✘'),
        ('1', '☕️'),
        ('2', '☕️☕️'),
        ('3', '☕️☕️☕️'),
        ('4', '☕️☕️☕️☕️'),
        ('5', '☕️☕️☕️☕️☕️'),
    ], validators=[DataRequired()])

    wifi = SelectField('Wifi', choices=[
        ('0', '✘'),
        ('1', '📶'),
        ('2', '📶📶'),
        ('3', '📶📶📶'),
        ('4', '📶📶📶📶'),
        ('5', '📶📶📶📶📶'),
    ], validators=[DataRequired()])

    power = SelectField('Power', choices=[
        ('0', '✘'),
        ('1', '🔌'),
        ('2', '🔌🔌'),
        ('3', '🔌🔌🔌'),
        ('4', '🔌🔌🔌🔌'),
        ('5', '🔌🔌🔌🔌🔌'),
    ], validators=[DataRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        name = form.data["cafe"]
        location = form.data["location"]
        open_time = form.data["open_time"]
        close_time = form.data["close_time"]
        coffee = int(form.data["coffee"])
        coffee = "✘" if coffee == 0 else "☕️" * coffee
        wifi = int(form.data["wifi"])
        wifi = "✘" if wifi == 0 else "📶" * wifi
        power = int(form.data["power"])
        power = "✘" if power == 0 else "🔌" * power
        with open("cafe-data.csv", "a") as f:
            f.writelines(f"{name},{location},{open_time},{close_time},{coffee},{wifi},{power}\n")
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
