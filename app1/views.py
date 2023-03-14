from django.shortcuts import render

# Create your views here.
def cricket(request):
    d={'name':'Virat'}
    return render(request,'cricket.html',context=d)