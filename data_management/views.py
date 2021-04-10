from django.shortcuts import render
from .models import *
from django.http import JsonResponse ,HttpResponse
import json

# Search based 
def search_data(request):
	search_data =  request.POST.get('search') if request.POST.get('search') else ''
	if search_data :
		products = Product.objects.filter(name__icontains = search_data).order_by('-id')[:20]
	else:
		products = ""
	return render(request,'index.html',locals())
    
def index(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Product.objects.filter(name__startswith=q)[:20]
        results = []
        for r in search_qs:
            results.append(r.name)
        data = json.dumps(results)
    else:
        data = 'failed'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

