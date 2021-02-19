from django.shortcuts import render

# Create your views here.
def front(request):
    return render(request, 'project/front.html')

def login(request):
    return render(request, 'project/login.html')

def register(request):
    return render(request, 'project/register.html')
