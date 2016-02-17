from django.shortcuts import render

from django.core.mail import send_mail

# importa o que tu precisar que fica no arquivo settings.py
from django.conf import settings

# pro form ali de baixo que vai pro html
from aula.forms import SignUpForm, ContactForm

# Create your views here.

#cria a view Home
def home(request):
    title = "Página Principal"

    # o SignUpForm veio do SignUpForm que esta no arquivo
    #forms
    # so funciona se ele estiver tudo ok, se nao, avisa erro
    #e nao funfa
    form = SignUpForm(request.POST or None)

    #variavel que passa os valores pro HTML
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
            "title": "Vlwww!"
        }

    return render(request, "home.html", context)



# view de contato que foi criada para enviar email...
def contact(request):

    #a variavel FORM recebe todos os valores do ContactForm, que esta no arquivo forms.py
    # esse arquivo forms.py foi criado pois como nao tem a necessidade de ter nada no banco de dados
    #no proprio form e criado o form e ele ja vem pra ca
    form = ContactForm(request.POST or None)

    # CASO o form seja valido, isso e, tudo completo e certim, faz as paradas aqui
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        # assunto do email
        subject = 'Site contact form'

        #abaixo parece confuso mas e basicamente, eu enviando email para eu mesmo, mas com o email de contato do cara
        # e o que ele escreveu

        #quem enviou o email
        from_email = settings.EMAIL_HOST_USER
        #para onde vei ser enviado
        to_email = [from_email]

        #mensagem que sera exibida no meu email, no caso, de onde veio, a mensagem e o nome do cara
        contact_message = "%s: %s de %s"%(form_email,form_message,form_full_name)

        #funcao que envia o email
        send_mail(subject, contact_message, from_email, to_email, fail_silently=False )

    #variavel que envia pro html uma outra variavel que e os forms
    context = {
        "form": form,
        "title": "Contato",
    }

    return render(request, "forms.html", context)







