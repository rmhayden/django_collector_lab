from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Finch
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form
    })

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
    return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']
  success_url = '/finches/'

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

# the {} argument is how python data is passed into this function

