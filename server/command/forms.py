from django import forms


class CommandForm(forms.Form):
    command = forms.CharField(max_length=200)
