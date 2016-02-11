from django.shortcuts import render

# pro form ali de baixo que vai pro html
from aula.forms import SignUpForm

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

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print (instance)
        context = {
            "title": "Thank you"
        }


    return render(request, "home.html", context)