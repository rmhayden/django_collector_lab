from django.shortcuts import render


# data usually comes from a model; temporary data below for now

finches = [
    {'name': 'darwin'},
    {'name': 'big bird'}
]

# Create your views here.
# (views in Django are like controllers in express)

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
# the {} argument is how python data is passed into this function