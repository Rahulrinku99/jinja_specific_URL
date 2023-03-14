from django.shortcuts import render

# Create your views here.
def football(request):
    d={'name':'messi'}
    return render(request,'cricket.html',context=d)