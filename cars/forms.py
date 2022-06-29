from django import forms

class AboutForm(forms.Form):
    model = forms.CharField(label='Model', initial='name model')
    color = forms.CharField(label='Color', initial='input color')
    year = forms.IntegerField(label='car year', initial='input car year')



class ModelsForm(forms.Form):
    model = forms.CharField(label='Model', initial='name model')
    year = forms.IntegerField(label='car year', initial='input car year')



class AccountForm(forms.Form):
    login = forms.CharField(label='Логин', initial='input login')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, initial='input password')

class ColorForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, initial='Please leave your comment')


