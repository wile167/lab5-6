from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-12345'

DATA = [
    {"id": 1, "name": "Ноутбук Pro 15", "price": 45000, "in_stock": True},
    {"id": 2, "name": "Миша Wireless G", "price": 1200, "in_stock": True},
    {"id": 3, "name": "Клавіатура Mech", "price": 3500, "in_stock": False},
]

# Завдання 5: Опис FlaskForm з валідаторами
class FeedbackForm(FlaskForm):
    name = StringField('ПІБ користувача', validators=[
        DataRequired(message="Обов'язкове поле"),
        Length(min=2, max=50, message="Довжина імені має бути від 2 до 50 символів")
    ])
    email = StringField('Електронна пошта', validators=[
        DataRequired(message="Обов'язкове поле"),
        Email(message="Некоректний формат email")
    ])
    category = SelectField('Категорія звернення', choices=[
        ('general', 'Загальне питання'),
        ('order', 'Питання по замовленню'),
        ('tech', 'Технічна підтримка')
    ])
    message = TextAreaField('Повідомлення', validators=[
        DataRequired(message="Обов'язкове поле"),
        Length(min=10, message="Повідомлення має містити щонайменше 10 символів")
    ])
    submit = SubmitField('Надіслати')

    # Кастомна валідація: перевірка на мінімальну кількість слів (не менше 3 слів)
    def validate_message(self, field):
        words = field.data.strip().split()
        if len(words) < 3:
            raise ValidationError("Повідомлення повинно містити щонайменше 3 слова.")

@app.route('/')
def index():
    return render_template('index.html', title="Головна", site_name="TechStore Flask", items_count=len(DATA), year=datetime.now().year)

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title="Каталог товарів", items=DATA, year=datetime.now().year)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash("Ваше повідомлення успішно надіслано!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', title="Зворотний зв'язок", form=form, year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)