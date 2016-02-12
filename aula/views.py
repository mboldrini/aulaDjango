from django.shortcuts import render

from django.core.mail import send_mail

# importa o que tu precisar que fica no arquivo settings.py
from django.conf import settings

# pro form ali de baixo que vai pro html
from aula.forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
    title = "Meu Titulo"

    # o SignUpForm veio do SignUpForm que esta no arquivo
    #forms
    # so funciona se ele estiver tudo ok, se nao, avisa erro
    #e nao funfa
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    # se o formulario e valido, caso nao tenha nenhum erro, executa
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "Usuario"
        instance.full_name = full_name

        instance.save()
        # se o form estiver tudo certo, a variavel TITLE muda o valor
        # e ela é exibida como "Thank you"
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)




def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s de %s"%(form_email,form_message,form_full_name)

        send_mail(subject, contact_message, from_email, to_email, fail_silently=False )

    context = {
        "form": form,
    }

    return render(request, "forms.html", context)







