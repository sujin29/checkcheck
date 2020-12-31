from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import*

# Create your views here.
def index(request):
    return render(request, "my_everyday_app/index.html")

def createHabbit(request):
    user_input_str = request.POST['habTitle']
    new_habbit = Habbit(hab_title = user_input_str)
    new_habbit.save()
    return HttpResponseRedirect(reverse('dashboard'))
    # return HttpResponse('create Habbit 할거야! ->'+user_input_str)

def dashboard(request):
    habbits = Habbit.objects.all()
    content = {'habbits' : habbits}
    return render(request, 'my_everyday_app/dashboard.html', content)