from django.shortcuts import render

from .models import Finch

# data usually comes from a model; temporary data below for now

# finches = [
#     {'name': 'darwin'},
#     {'name': 'big bird'}
# ]

# Create your views here.
# (views in Django are like controllers in express)

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {
        'finch': finch
    })

# the {} argument is how python data is passed into this function

