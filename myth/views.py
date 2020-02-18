from django.shortcuts import render
from .models import Region, Type, Being 
from django.contrib.auth.decorators import login_required
# Create your views here.

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'myth/region_list.html', {'regions': regions})

def type_list(request):
    types = Type.objects.all()
    return render(request, 'myth/type_list.html', {'types': types})

def single_region(request, pk):
    region = Region.objects.get(id=pk)
    return render(request, 'myth/single_region.html', {'region': region})

def single_type(request, pk):
    single = Type.objects.get(id=pk)
    return render(request, 'myth/single_type.html', {'single': single})

def single_being(request, pk):
    god = Being.objects.get(id=pk)
    return render(request, 'myth/single_being.html', {'god': god})
