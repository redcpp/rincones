from django.shortcuts import render

def home(request):
    template = 'products/home.html'
    context = locals()
    return render(request, template, context)

