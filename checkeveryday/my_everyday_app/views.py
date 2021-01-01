from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import*

# Create your views here.
def index(request):
    return render(request, "my_everyday_app/index.html")

def createHabbit(request):
    habbit_title = request.POST['habTitle']
    habbit_method = request.POST['habMethod']

    new_habbit = Habbit(hab_title = habbit_title, hab_method= habbit_method)

    new_habbit.save()
    return HttpResponseRedirect(reverse('dashboard'))
    # return HttpResponse('create Habbit 할거야! ->'+user_input_str)

def dashboard(request):
    habbits = Habbit.objects.all()
    # checks = CheckHab.objects.all()
    content = {'habbits': habbits}
    return render(request, 'my_everyday_app/dashboard.html', content)