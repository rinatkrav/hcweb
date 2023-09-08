from django.shortcuts import render
from django.http import HttpResponse
from hcapp.models import Mclip, Mpic

# Create your views here.
def home(request):
    return render(request, 'hcapp/home.html')

def draft(request):
        return render(request, 'hcapp/draft.html')
