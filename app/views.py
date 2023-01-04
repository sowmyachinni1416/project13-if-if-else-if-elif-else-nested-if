from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':234,'b':356}
    return render(request,'operations.html',d)