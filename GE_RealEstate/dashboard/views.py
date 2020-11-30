from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
import requests


def index(request):

    listings = Listing.objects.all()

    context = {
        'listings' : listings
    }

    return render(request, 'dashboard/index.html', context)
    

def about(request):

    return render(request, 'dashboard/about.html', context)

def listings(request):


    return render(request, 'dashboard/listings.html')

def realtors(request):

    realtors = Realtor.objects.all()

    context = {
        'realtors' : realtors
    }

    return render(request, 'dashboard/realtors.html', context)