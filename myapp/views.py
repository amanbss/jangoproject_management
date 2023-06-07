from django.shortcuts import render

# Create your views here.
from myapp.models import query
def indexpage(request):
    x=query.objects.all()
    return render(request,"index.html")
def submitdata(request):
    if request.method=="POST":
        a=request.POST["name"]
        b=request.POST["password"]
        print(a,b)
        obj=query(name=a,password=b)
        obj.save()
        return render(request,"index.html")

