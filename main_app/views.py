from django.shortcuts import render

# Create your views here.
# (views in Django are like controllers in express)

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')