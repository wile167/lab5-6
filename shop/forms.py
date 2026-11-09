from django import forms

class FeedbackForm(forms.Form):
    CATEGORY_CHOICES = [
        ('general', 'Загальне питання'),
        ('order', 'Питання по замовленню'),
        ('tech', 'Технічна підтримка'),
    ]
    
    name = forms.CharField(
        label='ПІБ користувача',
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': "Введіть ваші ПІБ"})
    )
    email = forms.EmailField(
        label='Електронна пошта',
        widget=forms.EmailInput(attrs={'placeholder': "example@domain.com"})
    )
    category = forms.ChoiceField(
        label='Категорія звернення',
        choices=CATEGORY_CHOICES
    )
    message = forms.CharField(
        label='Повідомлення',
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': "Напишіть ваше повідомлення..."})
    )

    # Кастомна валідація: перевірка на мінімальну кількість слів (не менше 3 слів)
    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        words = message.strip().split()
        if len(words) < 3:
            raise forms.ValidationError("Повідомлення повинно містити щонайменше 3 слова.")
        return message