from django import forms
from django.core.validators import RegexValidator
from .models import ContactMessage

class ContactMassageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields =['name', 'contact_type', 'contact_value', 'message']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form_control', 'placeholder':'Ваше имя'}),
            'contact_type':forms.Select(attrs={'class': 'form-select'}),
            'contact_value':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email, телефон или ссылка на ВК'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'placeholder':'Ваше сообщение'}),
        }
        labels ={
            'name':'Имя',
            'contact_type':'Способ связи',
            'contact_value':'Контакт',
            'message':'Сообщение',
        }

    def clean(self):
        cleaned_data = super().clean()
        contact_type = cleaned_data.get('contact_type')
        contact_value = cleaned_data.get('contact_value', '')

        if not contact_value:
            raise forms.ValidationError('Укажите контакт для связи')

        elif contact_type == 'email':
            email_field = forms.EmailField()
            try:
                email_field.clean(contact_value)
            except forms.ValidationError:
                self.add_error('contact_value', 'Введите корректный email')

        elif contact_type == 'phone':
            validator = RegexValidator(
                regex=r'^[78]\d{10}$',
                message='Введите номер телефона из 11 цифр'
            )
            try:
                validator(contact_value)
            except forms.ValidationError as e:
                self.add_error('contact_value', e.message)
        elif contact_type == 'vk':
            if not('vk.com' in contact_value or 'vkontakte.ru' in contact_value):
                self.add_error('contact_value', 'Введите ссылку на профиль ВК')
            return cleaned_data