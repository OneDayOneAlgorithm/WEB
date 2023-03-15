from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    
    context = {
        "라면":["라면",cnt,980*cnt],
        "홈":["홈",cnt,1500*cnt],
        "칙촉":["칙촉",cnt,2300*cnt],
        "식빵":["식빵",cnt,1800*cnt]
    }
    if thing == '라면':
        return render(request,'price.html',context['라면'])
    elif thing == '홈런볼':
        return render(request,'price.html',context['홈런볼'])
    elif thing == '칙촉':
        return render(request,'price.html',context['칙촉'])
    elif thing == '식빵':
        return render(request,'price.html',context['식빵'])
    else:
        return 
