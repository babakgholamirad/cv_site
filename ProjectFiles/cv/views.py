from django.shortcuts import render

# Create your views here.


def about(request):

    return render(request,'cv/about.html')

def test(request):

    return render(request,'cv/test.html')
