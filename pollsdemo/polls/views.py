from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Options
# Create your views here.


def Pollslist(request):
    list = Questions.objects.all()
    print(list,type(list))
    # return HttpResponse("列表页")
    return render(request,'polls/list.html',{'list':list})

def Choice(request,i):
    question = Questions.objects.get(pk = int(i))
    optlist = question.options_set.all()
    print(optlist,type(optlist))
    return render(request,'polls/choice.html',{'que':question,'optlist':optlist})

def ChoiceTool(request,i):
    opt = request.POST['options']
    question = Questions.objects.get(pk=int(i))
    optlist = question.options_set.all()
    thisopt = question.options_set.get(pk=int(opt))
    # print(thisopt,type(thisopt))
    thisopt.votes += 1
    thisopt.save()
    # return HttpResponse("投票成功")
    return render(request,'polls/votes.html',{'que':question,'optlist':optlist})
