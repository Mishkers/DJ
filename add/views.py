from django.shortcuts import render
from .models import Advert
from django.http import HttpResponse
from .forms import AdvertForm
# Create your views here.


def index(request):
    adverts = Advert.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def advert_post(request):
    form = AdvertForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)

