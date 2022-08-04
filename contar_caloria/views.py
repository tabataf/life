from asyncore import read
from django.shortcuts import render
from django.http import JsonResponse
import requests, json

from contar_caloria.models import TipoRefeicao
# Create your views here.

def pagina_inicial(request):
    alimento_digitado= request.GET.get('alimento')
    refeicao = TipoRefeicao.objects.all()
    alimento_digitado= alimento_digitado
    resultado= requests.get(f'https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={alimento_digitado}')
    consulta_alimento= json.loads(resultado.content)
    alimentos_filtrado = []
    for alimento in consulta_alimento:
        alimentos_filtrado.append({
            'caloria': alimento['calorias'],
            'descricao': alimento['descricao'],
            'quantidade': alimento['quantidade'],
        })
    context ={
        'consulta_alimento' : alimentos_filtrado,
        'refeicao': refeicao,
    }


    return render (request, "contar_caloria/pg_inicial.html",context)
