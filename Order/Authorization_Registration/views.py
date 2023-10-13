from django.shortcuts import render

# Create your views here.
def auth_func(request):
    return render(request, 'Authorization_Registration/authorization.html')

def reg_func(request):
    return render(request, 'Authorization_Registration/registration.html')
