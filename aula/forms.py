from django import forms

from aula.models import SignUp

class SignUpForm(forms.ModelForm):
    # organiza os forms na pg de admin do django
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

    #def clean_email(self):
        #email = self.cleaned_data.get('email')
        #return email