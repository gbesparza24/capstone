from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
import requests


def index(request):

    return render(request, 'dashboard/index.html')
    

def about(request):

    return render(request, 'dashboard/about.html')

def listings(request):

    return render(request, 'dashboard/listings.html')

def realtors(request):

    realtors = Realtor.objects.all()

    context = {
        'realtors' : realtors
    }

    return render(request, 'dashboard/realtors.html', context)