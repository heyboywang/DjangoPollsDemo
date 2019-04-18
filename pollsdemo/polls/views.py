from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def Pollslist(request):
    return HttpResponse("列表页")


