from django import forms

from aula.models import SignUp

# sem usar um modelo, e formado da forma explicita o form
#cria o formulario de contato, sem a necessidade de manter registro no DB
class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    # organiza os forms na pg de admin do django
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

