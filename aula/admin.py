from django.contrib import admin


# importa o form dos usuarios no adm
from aula.forms import SignUpForm
from aula.models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
    #class Meta:
    #    model = SignUp

admin.site.register(SignUp, SignUpAdmin)