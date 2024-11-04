from tempfile import template

from django.shortcuts import render
from numpy.distutils.from_template import template_name_re


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')