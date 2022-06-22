from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    is_married = forms.BooleanField()
    null_is_married = forms.NullBooleanField()
    address = forms.EmailField()
    ip_address = forms.GenericIPAddressField()
    link = forms.URLField()
    file_select = forms.FileField()
    file_select_image = forms.ImageField()
    data = forms.DateField()
    time = forms.TimeField()
    data_time = forms.SplitDateTimeField()
    numb = forms.FloatField()
    list1 = forms.ChoiceField(choices=((1, 'Kharkiv'), (2, 'Kyiv'), (3, 'Lviv')))

