from django.shortcuts import redirect, render
from django.http import HttpResponse
from Cadastro.forms import PasseiosForm
from .models import Cad_Passeios
# Create your views here.

def index(resquest):
    return HttpResponse("Olá Mundo! gora é Web!")

def listar_passeios(request):
    passeios = Cad_Passeios.objects.order_by('DataPasseio')
    return render(request,'lista_passeios.html', {'passeios':passeios})

def incluir_passeios(request):
    if request.method == 'POST':
        form = PasseiosForm(request.POST)
        if form.is_valid():
            form.save()
            return listar_passeios(request)
    form = PasseiosForm()
    return render(request,'incluir_Passeios.html', {'formulario': form})

def alterar_passeio(request, codigo):
    passeio = Cad_Passeios.objects.get(id = codigo)

    if request.method == 'POST':
        form = PasseiosForm(request.POST , instance=passeio)
        if form.is_valid():
            form.save()
            return redirect('listar_passeios')

    form = PasseiosForm(instance=passeio)
    return render (request, 'incluir_Passeios.html',{'formulario': form})

def excluir_passeio(request, codigo):
    passeio = Cad_Passeios.objects.get(id=codigo)
    
    Cad_Passeios.delete(passeio)

    return redirect('listar_passeios')
