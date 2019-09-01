from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def list_view(request):
	url = "https://pokeapi.co/api/v2/pokemon/"
	if request.GET:
		url = request.GET.get('next')
	
	response = requests.get(url).json()

	context = {
		'pokes': response
	}
	return render(request, "list.html", context)

def detail_view(request):
	url = request.GET.get('detail')
	response = requests.get(url).json()

	context = {
		'poke_det': response,
	}
	
	return render(request, 'detail.html', context)

	# return JsonResponse(response)





