from django.shortcuts import render , HttpResponseRedirect
from .forms import tractor_details
from .models import Farm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = tractor_details(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ph = fm.cleaned_data['phone']
            tb = fm.cleaned_data['tractor_brand']
            ml = fm.cleaned_data['model']
            ti = fm.cleaned_data['tractor_implements']
            reg = Farm(name=nm ,email =em , phone = ph , tractor_brand = tb , model = ml ,  tractor_implements = ti)
            reg.save()
            messages.success(request , "Farmer details added successfully!")
            return HttpResponseRedirect('/')
    else:
        fm = tractor_details()
    recd = Farm.objects.all().order_by('-id')
    return render(request , 'index.html' , {'form' :fm ,'recorddata':recd })


def delete(request , id):
    if request.method == 'POST':
        pi = Farm.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request , id):
    if request.method == 'POST':
        pi = Farm.objects.get(pk=id)
        fm = tractor_details(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request , "Record update successfully!")
            return HttpResponseRedirect('/')
    else:
        pi = Farm.objects.get(pk=id)
        fm = tractor_details(instance=pi)
    return render(request , 'update.html' ,{'form' :fm})

