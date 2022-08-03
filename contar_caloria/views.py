from django.shortcuts import render
from django.http import JsonResponse
import requests, json

from contar_caloria.models import TipoRefeicao
# Create your views here.

def pagina_inicial(request):
    alimento_digitado= request.GET.get('alimento')
    refeicao = TipoRefeicao.objects.all()
    alimento_digitado= alimento_digitado
    consulta_alimento= requests.get(f'https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={alimento_digitado}')
    consulta_alimento= json.load(consulta_alimento.json())
    context ={
        'consulta_alimento' : consulta_alimento,
        'refeicao': refeicao,
    }

    return render (request, "contar_caloria/pg_inicial.html",context)

def alimento(request):
    return JsonResponse(context)

# def listar_alimento(request, id):
#     refeicao = TipoRefeicao.objects.all()
#     context ={
#         'refeicao' : refeicao
#     }
#     return render(request, 'contar_caloria/pg_inicial.html', context)