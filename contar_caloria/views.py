from django.shortcuts import render
from django.http import JsonResponse
import requests

from contar_caloria.models import TipoRefeicao
# Create your views here.

def pagina_inicial(request):
    refeicao = TipoRefeicao.objects.all()
    context ={
        'refeicao' : refeicao
    }

    return render (request, "contar_caloria/pg_inicial.html",context)

def alimento(request):
    alimento_digitado= 'frango'
    consulta_alimento= requests.get(f'https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={alimento_digitado}')
    consulta_alimento= consulta_alimento.json()
    context ={
        'alimento' : consulta_alimento
    }
    return JsonResponse(context)

# def listar_alimento(request, id):
#     refeicao = TipoRefeicao.objects.all()
#     context ={
#         'refeicao' : refeicao
#     }
#     return render(request, 'contar_caloria/pg_inicial.html', context)