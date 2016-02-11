from django.contrib import admin



from aula.models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)