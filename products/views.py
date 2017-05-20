from django.shortcuts import render

def home(request):
    username_is = 'Juan' if request.user.is_authenticated() else 'Anon'

    context = {'username_is': username_is}
    template = 'products/home.html'
    return render(request, template, context)

