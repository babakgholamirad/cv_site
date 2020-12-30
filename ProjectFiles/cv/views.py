from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request,'cv/home.html')

def test(request):

    return render(request,'cv/test.html')
