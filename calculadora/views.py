from django.shortcuts import render

# Create your views here.

def calculadora(request):
    return render(request, 'preparacao.html')
def quem_somos(request):
    return render(request, 'quem somos.html')