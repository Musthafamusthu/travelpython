from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from.models import Place1
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Place1.objects.all()
    #return HttpResponse("hello world")
    #name='ARITHMETIC OPERATIONS'
    return render(request,'index.html',{'result':obj,'result1':obj1})
# def demo1(request):
#     obj1=Place1.objects.all()
#     return render(request,'index.html',{'result1':obj1})
#def addition(request):
  #  n1=float(request.GET['num1'])
   # n2=float(request.GET['num2'])
    #add=n1+n2
    #mul=n1*n2
    #sub=n1-n2
    #div=n1/n2
    #@return render(request,'result.html',{'addition':add,'multiplication':mul,'subtraction':sub,'division':div})
#def contact(request):
 #   return HttpResponse("hello i am contact")