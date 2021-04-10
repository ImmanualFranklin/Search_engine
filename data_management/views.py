from django.shortcuts import render
from .models import *

# Create your views here.


def search_data(request):
	search_data =  request.POST.get('search') if request.POST.get('search') else ''
	products = Product.objects.filter(name__icontains = search_data).order_by('-id')[:20]
	return render(request,'index.html',locals())
    