from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Automato, ExpressaoRegular, MaquinaTuring
from .forms import FormSequencia, FormAutomato, FormExpressaoRegular, FormMaquinaTuring
import os

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def automatosFinitos(request):
    context = {'automatosFinitos': Automato.objects.all()}
    return render(request, 'website/automatosFinitos.html', context)

def novoAutomato(request):
    form = FormAutomato(request.POST or None)
    if form.is_valid():
        novoAutomato = form.save()
        novoAutomato.filename = str(novoAutomato.nome).replace(' ', '_')
        novoAutomato.desenharDiagrama()
        novoAutomato.save()
        return HttpResponseRedirect(reverse('website:automatosFinitos'))

    context = {'form': form}

    return render(request, 'website/novoAutomato.html', context)

def detalhesAutomato(request, automato_id):
    sequencia = None
    resultado = None

    form = FormSequencia(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Automato.objects.get(id=automato_id).validarSequencia(sequencia)

    context = {
        'automato': Automato.objects.get(id=automato_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form
    }
    return render(request, 'website/detalhesAutomato.html', context)

def editarAutomato(request, automato_id):
    instance = Automato.objects.get(id=automato_id)
    form = FormAutomato(request.POST or None, instance=instance)
    if form.is_valid():
        automato = form.save()
        os.rename(f"website/static/website/images/afd/{automato.filename}", f"website/static/website/images/afd/{str(automato.nome).replace(' ', '_')}")
        os.rename(f"website/static/website/images/afd/{automato.filename}.svg", f"website/static/website/images/afd/{str(automato.nome).replace(' ', '_')}.svg")
        automato.filename = str(automato.nome).replace(' ', '_')
        automato.desenharDiagrama()
        automato.save()
        return HttpResponseRedirect(reverse('website:automatosFinitos'))

    context = {'form': form, 'automato_id': automato_id}
    return render(request, 'website/editarAutomato.html', context)

def apagarAutomato(request, automato_id):
    automato = MaquinaTuring.objects.get(id=automato_id)
    os.remove(f"website/static/website/images/afd/{str(automato.filename).replace(' ', '_')}.svg")
    os.remove(f"website/static/website/images/afd/{str(automato.filename).replace(' ', '_')}")
    Automato.objects.filter(id=automato_id).delete()
    context = {'automatosFinitos': Automato.objects.all()}
    return render(request, 'website/automatosFinitos.html', context)

def expressoesRegulares(request):
    context = {'expressoesRegulares': ExpressaoRegular.objects.all()}
    return render(request, 'website/expressoesRegulares.html', context)

def novaExpressao(request):
    form = FormExpressaoRegular(request.POST or None)
    if form.is_valid():
        novaExpressao = form.save()
        novaExpressao.save()
        return HttpResponseRedirect(reverse('website:expressoesRegulares'))

    context = {'form': form}

    return render(request, 'website/novaExpressao.html', context)

def detalhesExpressao(request, expressao_id):
    sequencia = None
    resultado = None

    form = FormSequencia(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = ExpressaoRegular.objects.get(id=expressao_id).validarSequencia(sequencia)

    context = {
        'expressao': ExpressaoRegular.objects.get(id=expressao_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form
    }
    return render(request, 'website/detalhesExpressao.html', context)

def editarExpressao(request, expressao_id):
    instance = ExpressaoRegular.objects.get(id=expressao_id)
    form = FormExpressaoRegular(request.POST or None, instance=instance)
    if form.is_valid():
        expressao = form.save()
        expressao.save()
        return HttpResponseRedirect(reverse('website:expressoesRegulares'))

    context = {'form': form, 'expressao_id': expressao_id}
    return render(request, 'website/editarExpressao.html', context)

def apagarExpressao(request, expressao_id):
    ExpressaoRegular.objects.filter(id=expressao_id).delete()
    context = {'expressoesRegulares': ExpressaoRegular.objects.all()}
    return render(request, 'website/expressoesRegulares.html', context)

def maquinasTuring(request):
    context = {'maquinasTuring': MaquinaTuring.objects.all()}
    return render(request, 'website/maquinasTuring.html', context)

def novaMaquina(request):
    form = FormMaquinaTuring(request.POST or None)
    if form.is_valid():
        novaMaquina = form.save()
        novaMaquina.filename = str(novaMaquina.nome).replace(' ', '_')
        novaMaquina.desenharDiagrama()
        novaMaquina.save()
        return HttpResponseRedirect(reverse('website:maquinasTuring'))

    context = {'form': form}

    return render(request, 'website/novaMaquina.html', context)

def detalhesMaquina(request, maquina_id):
    sequencia = None
    resultado = None

    maquina = MaquinaTuring.objects.get(id=maquina_id)
    form = FormSequencia(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = maquina.validarSequencia(sequencia)
        maquina.save()

    context = {
        'maquina': MaquinaTuring.objects.get(id=maquina_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form
    }
    return render(request, 'website/detalhesMaquina.html', context)

def editarMaquina(request, maquina_id):
    instance = MaquinaTuring.objects.get(id=maquina_id)
    form = FormMaquinaTuring(request.POST or None, instance=instance)
    if form.is_valid():
        maquina = form.save()
        os.rename(f"website/static/website/images/mt/{maquina.filename}", f"website/static/website/images/mt/{str(maquina.nome).replace(' ', '_')}")
        os.rename(f"website/static/website/images/mt/{maquina.filename}.svg", f"website/static/website/images/mt/{str(maquina.nome).replace(' ', '_')}.svg")
        maquina.filename = str(maquina.nome).replace(' ', '_')
        maquina.desenharDiagrama()
        maquina.save()
        return HttpResponseRedirect(reverse('website:maquinasTuring'))

    context = {'form': form, 'maquina_id': maquina_id}
    return render(request, 'website/editarMaquina.html', context)

def apagarMaquina(request, maquina_id):
    maquina = MaquinaTuring.objects.get(id=maquina_id)
    os.remove(f"website/static/website/images/mt/{str(maquina.filename).replace(' ', '_')}.svg")
    os.remove(f"website/static/website/images/mt/{str(maquina.filename).replace(' ', '_')}")
    MaquinaTuring.objects.filter(id=maquina_id).delete()
    context = {'maquinasTuring': MaquinaTuring.objects.all()}
    return render(request, 'website/maquinasTuring.html', context)