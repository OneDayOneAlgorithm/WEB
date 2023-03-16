from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):

    if thing == '라면':
        context = {
            'thing':'라면',
            'cnt' : cnt,
            'total' : 980*cnt
        }
    elif thing == '홈런볼':
        context = {
            'thing':'홈런볼',
            'cnt' : cnt,
            'total' : 1500*cnt
        }
    elif thing == '칙촉':
        context = {
            'thing':'칙촉',
            'cnt' : cnt,
            'total' : 2300*cnt
        }
    elif thing == '식빵':
        context = {
            'thing':'식빵',
            'cnt' : cnt,
            'total' : 1800*cnt
        }
    else:
        context = {
            'thing' : thing
        }
    return render(request,'price.html',context)
