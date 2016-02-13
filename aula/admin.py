from django.contrib import admin


# importa o form dos usuarios no adm
from aula.forms import SignUpForm, MeuModelForm
from aula.models import SignUp, MeuModel

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
    #class Meta:
    #    model = SignUp

admin.site.register(SignUp, SignUpAdmin)




class MeuModelAdmin(admin.ModelAdmin):
    list_display = [ "nome", "email"]
    form = MeuModelForm

admin.site.register(MeuModel, MeuModelAdmin)